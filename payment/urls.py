from django.urls import path
from .views import (
    BkashCreatePaymentView,
    BkashExecutePaymentView,
    BkashQueryPaymentView,
    BkashCreateAgreementView,
    BkashExecuteAgreementView,
    BkashQueryAgreementView,
    BkashCancelAgreementView,
    BkashRecurringPaymentView,
)

urlpatterns = [
    path("create/", BkashCreatePaymentView.as_view(), name="bkash-create"),
    path("execute/", BkashExecutePaymentView.as_view(), name="bkash-execute"),
    path("query/", BkashQueryPaymentView.as_view(), name="bkash-query"),
    # Recurring payment (agreement) endpoints
    path("agreement/create/", BkashCreateAgreementView.as_view(), name="bkash-agreement-create"),
    path("agreement/execute/", BkashExecuteAgreementView.as_view(), name="bkash-agreement-execute"),
    path("agreement/query/", BkashQueryAgreementView.as_view(), name="bkash-agreement-query"),
    path("agreement/cancel/", BkashCancelAgreementView.as_view(), name="bkash-agreement-cancel"),
    path("recurring/payment/", BkashRecurringPaymentView.as_view(), name="bkash-recurring-payment"),
]
