from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PaymentCreateSerializer, AgreementCreateSerializer, RecurringPaymentSerializer
from .bkash import BkashAPI


class BkashCreatePaymentView(APIView):
    def post(self, request):
        serializer = PaymentCreateSerializer(data=request.data)
        if serializer.is_valid():
            bkash = BkashAPI()
            result = bkash.create_payment(
                amount=serializer.validated_data["amount"],
                invoice=serializer.validated_data["invoice"],
            )
            return Response(result)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BkashExecutePaymentView(APIView):
    def post(self, request):
        payment_id = request.data.get("paymentID")
        if not payment_id:
            return Response({"error": "paymentID is required"}, status=400)
        bkash = BkashAPI()
        result = bkash.execute_payment(payment_id)
        return Response(result)


class BkashQueryPaymentView(APIView):
    def post(self, request):
        payment_id = request.data.get("paymentID")
        if not payment_id:
            return Response({"error": "paymentID is required"}, status=400)
        bkash = BkashAPI()
        result = bkash.query_payment(payment_id)
        return Response(result)


class BkashCreateAgreementView(APIView):
    def post(self, request):
        serializer = AgreementCreateSerializer(data=request.data)
        if serializer.is_valid():
            bkash = BkashAPI()
            result = bkash.create_agreement(
                payer_reference=serializer.validated_data["payer_reference"],
            )
            return Response(result)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BkashExecuteAgreementView(APIView):
    def post(self, request):
        payment_id = request.data.get("paymentID")
        if not payment_id:
            return Response({"error": "paymentID is required"}, status=400)
        bkash = BkashAPI()
        result = bkash.execute_agreement(payment_id)
        return Response(result)


class BkashQueryAgreementView(APIView):
    def post(self, request):
        agreement_id = request.data.get("agreementID")
        if not agreement_id:
            return Response({"error": "agreementID is required"}, status=400)
        bkash = BkashAPI()
        result = bkash.query_agreement(agreement_id)
        return Response(result)


class BkashCancelAgreementView(APIView):
    def post(self, request):
        agreement_id = request.data.get("agreementID")
        if not agreement_id:
            return Response({"error": "agreementID is required"}, status=400)
        bkash = BkashAPI()
        result = bkash.cancel_agreement(agreement_id)
        return Response(result)


class BkashRecurringPaymentView(APIView):
    def post(self, request):
        serializer = RecurringPaymentSerializer(data=request.data)
        if serializer.is_valid():
            bkash = BkashAPI()
            result = bkash.create_recurring_payment(
                agreement_id=serializer.validated_data["agreement_id"],
                payer_reference=serializer.validated_data["payer_reference"],
                amount=serializer.validated_data["amount"],
                invoice=serializer.validated_data["invoice"],
            )
            return Response(result)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
