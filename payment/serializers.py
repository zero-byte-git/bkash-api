from rest_framework import serializers


class PaymentCreateSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    invoice = serializers.CharField()


class AgreementCreateSerializer(serializers.Serializer):
    payer_reference = serializers.CharField()


class RecurringPaymentSerializer(serializers.Serializer):
    agreement_id = serializers.CharField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    invoice = serializers.CharField()
