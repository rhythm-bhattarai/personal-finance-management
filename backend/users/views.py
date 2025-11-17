from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status, viewsets
from .services import AuthService
from django.core.exceptions import ValidationError
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenRefreshView

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
        
    # POST /users/login/ - User login
    @action(detail=False, methods=['post'])
    def login(self, request, format='json'):
        email = request.data.get('email')
        password = request.data.get('password')

        if email is None or password is None:
            return Response({'error': 'Please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            tokens = AuthService.login_user(email, password)
            response =  Response(tokens, status=status.HTTP_200_OK)

            response.set_cookie(
                key='refresh_token',
                value=tokens.get('refresh'),
                httponly=True,
                samesite='None',
                secure=True,
                max_age=7*24*60*60  # 7 days
            )

            return response
        
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def profile(self, request, format='json'):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class RefreshTokenView(APIView):
    
    permission_classes = [AllowAny]

    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')

        if refresh_token is None:
            return Response({'error': 'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            refresh = AuthService.refresh_token(refresh_token)
            access = refresh.access_token
            return Response({'access': str(access)}, status=status.HTTP_200_OK)
        
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
