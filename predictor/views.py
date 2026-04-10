from django.shortcuts import render
import requests

def rto_check_view(request):
    result = None
    if request.method == 'POST':
        data = {
            "paymentMethodRegistrationFailure": int(request.POST.get('reg_fail',0)),
            "paymentMethodType": int(request.POST.get('pm_type',0)),
            "paymentMethodProvider":int(request.POST.get('pm_provider',0)),
            "transactionAmount": float(request.POST.get('amount',0)),
            "transactionFailed": int(request.POST.get('trans_fail' ,0)) ,
            "orderState": int(request.POST.get('order_state',0)),
            "No_Transaction": int(request.POST.get('n_trans' ,0)),
            "No_Orders": int(request.POST.get('n_orders',0)),
            "No_Payments": int(request.POST.get('n_payments',0)),
        }

        try:
            response = requests.post("http:127.0.0.1:8000/predict" , json = data)
            if response.status_code == 200:
                result = response.json()
            else:
                result ={"error":f"API ERROR:{response.status_code}"}
        except Exception as e:
            result = {"error":"FastAPI Server is Offline"}

    return render(request, 'predictor/index.html' , {'result': result})