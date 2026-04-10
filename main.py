from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="Razorpay RTO Predictor API")
model = joblib.load("rto_model.pkl")


class TransactionData(BaseModel):
    paymentMethodRegistrationFailure: int
    paymentMethodType: int
    paymentMethodProvider: int
    transactionAmount: float
    transactionFailed: int
    orderState: int
    No_Transactions: int
    No_Orders: int
    No_Payments: int


@app.get("/")
def read_root():
    return {"status": "RTO Prediction API is online"}


@app.post("/predict")
def predict_rto(data: TransactionData):
    input_df = pd.DataFrame([data.model_dump()])

    cols = [
        "paymentMethodRegistrationFailure",
        "paymentMethodType",
        "paymentMethodProvider",
        "transactionAmount",
        "transactionFailed",
        "orderState",
        "No_Transactions",
        "No_Orders",
        "No_Payments",
    ]
    input_df = input_df[cols]
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    return {"is_rto_risk": int(prediction), "risk_score": round(float(probability), 4)}
