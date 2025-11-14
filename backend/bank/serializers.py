from rest_framework import serializers
from .models import AccountDetails, AmountDetails

class AccountDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountDetails
        fields = ['id', 'bank_name', 'account_number', 'bank_user', 'created_at', 'updated_at']
        extra_kwargs = {
            'bank_user': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }

        def create(self, validated_data):
            user = self.context['request'].user
            return AccountDetails.objects.create(bank_user=user, **validated_data)
        


class AmountDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmountDetails
        fields = ['id', 'account', 'balance', 'last_updated']
        extra_kwargs = {
            'last_updated': {'read_only': True},
        }

    def validate_balance(self, value):
        if value < 0:
            raise serializers.ValidationError("Balance cannot be negative.")
        return value
    
    def validate_account(self, value):
        account = value.get('account')
        user = self.context['request'].user
        if account.bank_user != user:
            raise serializers.ValidationError("You do not have permission to access this account.")
        return value

    def create(self, validated_data):
        return AmountDetails.objects.create(**validated_data)