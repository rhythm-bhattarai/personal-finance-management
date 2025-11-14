from .models import AccountDetails

class AccountService:

    def create_account(bank_name, account_number, user):
        account = AccountDetails.objects.create(
            bank_name=bank_name,
            account_number=account_number,
            bank_user=user
        )
        return account