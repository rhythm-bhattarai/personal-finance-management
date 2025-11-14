from rest_framework import viewsets, permissions
from .models import AccountDetails, AmountDetails
from .serializers import AccountDetailsSerializer, AmountDetailsSerializer
from rest_framework.exceptions import PermissionDenied

class AccountDetailsViewSet(viewsets.ModelViewSet):

    serializer_class = AccountDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(bank_user=self.request.user)

    def get_queryset(self):
        return AccountDetails.objects.filter(bank_user=self.request.user)
    

class AmountDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = AmountDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return AmountDetails.objects.filter(account__bank_user=self.request.user)

    def perform_create(self, serializer):
        account = serializer.validated_data.get('account')

        if account.bank_user != self.request.user:
            raise PermissionDenied("You do not have permission to add AmountDetails to this account.")

        serializer.save()