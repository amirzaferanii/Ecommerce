from django.shortcuts import redirect, get_object_or_404, render
import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
import json
from django.views import View
from Account.models import Address
from cart.models import Order
from Ecommerce import settings

if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'

ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

amount = 1000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
phone = 'YOUR_PHONE_NUMBER'  # Optional
CallbackURL = 'http://127.0.0.1:8000/zarinpal/verify/'


class SendRequestPayment(LoginRequiredMixin,View):
    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk, user=request.user)
        request.session['order_id'] = str(order.id)
        request.session.save()
        address = get_object_or_404(Address, pk=request.POST.get('address'), user=request.user)
        order.address = f'{address.address} - {address.phone} - {address.fullname}'
        order.save()
        amount = float(order.total_price)
        description = f'Payment for order {order.id}'
        phone = request.user.phone
        data = {"MerchantID": settings.MERCHANT, "Amount": amount, "Description": description, "Phone": phone, "CallbackURL": CallbackURL,}
        headers = {'content-type': 'application/json', 'content-length': str(len(json.dumps(data)))}
        try:
            response = requests.post(ZP_API_REQUEST, json=data, headers=headers, timeout=10)
            if response.status_code == 200:
                response_data = response.json()
                if response_data['Status'] == 100:
                    return redirect(ZP_API_STARTPAY + str(response_data['Authority']))
                else:
                    return JsonResponse({'status': False, 'code': str(response_data['Status'])})
            else:
                return JsonResponse({'status': False, 'code': 'Invalid response status'})
        except requests.exceptions.Timeout:
            return JsonResponse({'status': False, 'code': 'timeout'})
        except requests.exceptions.ConnectionError:
            return JsonResponse({'status': False, 'code': 'connection error'})


class VerifyView(View):
    def get(self, request):
        order_id = request.session["order_id"]
        order = Order.objects.get(id=str(order_id))
        def verify(authority):
            data = {"MerchantID": settings.MERCHANT, "Amount": order.total_price, "Authority": authority,}
            data = json.dumps(data)
            headers = {'content-type': 'application/json', 'content-length': str(len(data))}
            response = requests.post(ZP_API_VERIFY, data=data, headers=headers)

            if response.status_code == 200:
                order.is_paid = True
                order.save()
                response = response.json()
                if response['Status'] == 100:
                    context = {'RefID': response.get('RefID'), 'amount': order.total_price}
                    return render(request, 'zarinpal/succses_pay.html',context)
                else:
                    return render(request, 'zarinpal/fail_pay.html')
            else:
                return JsonResponse({'status': False, 'code': response.status_code})

        authority = request.GET.get('Authority')
        status = request.GET.get('Status')
        if status == 'OK':
            return verify(authority)
        else:
            return render(request, 'zarinpal/fail_pay.html')

