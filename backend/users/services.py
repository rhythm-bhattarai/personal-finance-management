from .models import User
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

class AuthService:
    def register_user(username, email, password, first_name, last_name):
        user = User.objects.create(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save()
        return user

    def login_user(email, password):
        try:
            user = User.objects.get(email=email)
        
        except User.DoesNotExist:
            raise ValidationError("Invalid email or password")
    
        if not user.check_password(password):
            raise ValidationError("Invalid email or password")
        
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
    