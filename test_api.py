import requests
import json

URL = "http://127.0.0.1:8000/predict"


def check_transaction(name, data):
    print(f"\n---TESTING PROFILE : {name} ---")
    response = requests.post(URL, json=data)

    if response.status_code == 200:
        result = response.json()
        risk = "HIGH RISK" if result["is_rto_risk"] == 1 else "LOW RISK"
        print(f"Predicion: {risk}")
        print(f"Confidence Score: {result['risk_score']*100:.2f}%")

    else:
        print(f"Error: {response.status_code}")
        print(response.text)


good_user = {
    "paymentMethodRegistrationFailure": 0,
    "paymentMethodType": 1,
    "paymentMethodProvider": 2,
    "transactionAmount": 20.0,
    "transactionFailed": 0,
    "orderState": 1,
    "No_Transactions": 1,
    "No_Orders": 1,
    "No_Payments": 1,
}

bad_user = {
    "paymentMethodRegistrationFailure": 1,
    "paymentMethodType": 0,
    "paymentMethodProvider": 1,
    "transactionAmount": 500.0,
    "transactionFailed": 1,
    "orderState": 0,
    "No_Transactions": 8,
    "No_Orders": 8,
    "No_Payments": 8,
}

if __name__ == "__main__":
    check_transaction("Loyal Customer", good_user)
    check_transaction("Suspicious New User", bad_user)
