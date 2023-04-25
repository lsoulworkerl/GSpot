from apps.base.fields import MoneySerializerField
from apps.base.serializer import PaymentServiceSerializer
from django.core.validators import MinValueValidator
from rest_framework import serializers

from .models import Account


class PaymentCommissionSerializer(PaymentServiceSerializer):
    payment_amount = MoneySerializerField(
        validators=[MinValueValidator(0, message='Insufficient Funds')],
    )


class BalanceIncreaseSerializer(PaymentCommissionSerializer):
    user_uuid = serializers.UUIDField()
    return_url = serializers.URLField()


class AccountSerializer(serializers.ModelSerializer):
    user_uuid = serializers.UUIDField()

    class Meta:
        model = Account
        fields = ('user_uuid',)