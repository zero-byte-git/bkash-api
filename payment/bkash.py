import requests
from django.conf import settings


class BkashAPI:
    def __init__(self):
        self.app_key = settings.BKASH_APP_KEY
        self.app_secret = settings.BKASH_APP_SECRET
        self.username = settings.BKASH_USERNAME
        self.password = settings.BKASH_PASSWORD
        self.base_url = settings.BKASH_BASE_URL
        self.token = self.get_token()

    def get_token(self):
        url = f"{self.base_url}/tokenized/checkout/token/grant"
        headers = {
            "Content-Type": "application/json",
            "username": self.username,
            "password": self.password,
        }
        data = {"app_key": self.app_key, "app_secret": self.app_secret}
        response = requests.post(url, headers=headers, json=data)
        return response.json().get("id_token")

    def create_payment(self, amount, invoice):
        url = f"{self.base_url}/tokenized/checkout/create"
        headers = {
            "Content-Type": "application/json",
            "authorization": self.token,
            "x-app-key": self.app_key,
        }
        data = {
            "mode": "0011",
            "payerReference": " ",
            "callbackURL": settings.BKASH_CALLBACK_URL,
            "amount": str(amount),
            "currency": "BDT",
            "intent": "sale",
            "merchantInvoiceNumber": invoice,
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json()

    def execute_payment(self, payment_id):
        url = f"{self.base_url}/tokenized/checkout/execute"
        headers = {
            "Content-Type": "application/json",
            "authorization": self.token,
            "x-app-key": self.app_key,
        }
        response = requests.post(url, headers=headers, json={"paymentID": payment_id})
        return response.json()

    def query_payment(self, payment_id):
        url = f"{self.base_url}/tokenized/checkout/payment/status"
        headers = {
            "Content-Type": "application/json",
            "authorization": self.token,
            "x-app-key": self.app_key,
        }
        response = requests.post(url, headers=headers, json={"paymentID": payment_id})
        return response.json()

    def create_agreement(self, payer_reference):
        """Create a recurring payment agreement (mode 0000)."""
        url = f"{self.base_url}/tokenized/checkout/create"
        headers = {
            "Content-Type": "application/json",
            "authorization": self.token,
            "x-app-key": self.app_key,
        }
        data = {
            "mode": "0000",
            "payerReference": payer_reference,
            "callbackURL": settings.BKASH_CALLBACK_URL,
            "amount": "0",
            "currency": "BDT",
            "intent": "sale",
            "merchantInvoiceNumber": "agreement",
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json()

    def execute_agreement(self, payment_id):
        """Execute/confirm an agreement after user approval."""
        url = f"{self.base_url}/tokenized/checkout/execute"
        headers = {
            "Content-Type": "application/json",
            "authorization": self.token,
            "x-app-key": self.app_key,
        }
        response = requests.post(url, headers=headers, json={"paymentID": payment_id})
        return response.json()

    def query_agreement(self, agreement_id):
        """Query the status of an agreement."""
        url = f"{self.base_url}/tokenized/checkout/agreement/status"
        headers = {
            "Content-Type": "application/json",
            "authorization": self.token,
            "x-app-key": self.app_key,
        }
        response = requests.post(url, headers=headers, json={"agreementID": agreement_id})
        return response.json()

    def cancel_agreement(self, agreement_id):
        """Cancel an active agreement."""
        url = f"{self.base_url}/tokenized/checkout/agreement/cancel"
        headers = {
            "Content-Type": "application/json",
            "authorization": self.token,
            "x-app-key": self.app_key,
        }
        response = requests.post(url, headers=headers, json={"agreementID": agreement_id})
        return response.json()

    def create_recurring_payment(self, agreement_id, amount, invoice):
        """Charge against an existing agreement (mode 0001)."""
        url = f"{self.base_url}/tokenized/checkout/create"
        headers = {
            "Content-Type": "application/json",
            "authorization": self.token,
            "x-app-key": self.app_key,
        }
        data = {
            "mode": "0001",
            "agreementID": agreement_id,
            "payerReference": " ",
            "callbackURL": settings.BKASH_CALLBACK_URL,
            "amount": str(amount),
            "currency": "BDT",
            "intent": "sale",
            "merchantInvoiceNumber": invoice,
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json()
