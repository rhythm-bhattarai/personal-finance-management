from django.db import models
from users.models import User

class AccountDetails(models.Model):
    bank_name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=20, unique=True)
    bank_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='account_details')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.bank_name} - ({self.account_number}) for {self.bank_user.username}"
    
class AmountDetails(models.Model):
    account = models.ForeignKey(AccountDetails, on_delete=models.CASCADE, related_name='amount_bank_account')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Balance of {self.balance} in account {self.account.account_number}"

class TransactionDetails(models.Model):
    TRANSACTION_TYPES = [
        ('DEPOSIT', 'Deposit'),
        ('WITHDRAWAL', 'Withdrawal'),
        ('TRANSFER', 'Transfer'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transaction_user')
    account = models.ForeignKey(AccountDetails, on_delete=models.CASCADE, related_name='transaction_bank_account')
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} of {self.amount} by {self.user.username} on {self.timestamp}"