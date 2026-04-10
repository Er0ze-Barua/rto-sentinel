import pandas as pd
from pandas.core.arrays import categorical
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib


def prepare_data():
    df_trans = pd.read_csv("archive (6)/cust_transaction_details (1).csv")
    df_cust = pd.read_csv("archive (6)/Customer_DF (1).csv")

    df = pd.merge(df_trans, df_cust, on="customerEmail", how="inner")

    cols_to_drop = [
        "customerEmail",
        "transactionId",
        "orderId",
        "paymentMethodId",
        "customerIPAddress",
        "customerBillingAddress",
        "customerPhone",
        "customerDevice",
        "Unnamed: 0_x",
        "Unnamed: 0_y",
    ]

    df.drop(columns=cols_to_drop, inplace=True)

    le = LabelEncoder()
    categorical_cols = ["paymentMethodType", "paymentMethodProvider", "orderState"]

    for col in categorical_cols:
        df[col] = le.fit_transform(df[col].astype(str))

    print("Current Columns:", df.columns.tolist())
    df["Fraud"] = df["Fraud"].astype(int)

    X = df.drop("Fraud", axis=1)
    y = df["Fraud"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print(f"Training set size: {X_train.shape} ")
    print(f"Testing set size: {X_test.shape}")

    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    prepare_data()
    # Add this to data_prep.py to see how it's encoding things
le = LabelEncoder()
df_test = pd.read_csv(
    "archive (6)/cust_transaction_details (1).csv"
)  # or your merged df
le.fit(df_test["orderState"].astype(str))
print("OrderState Mapping:", dict(zip(le.classes_, le.transform(le.classes_))))

# Also check the target distribution
df_cust = pd.read_csv("archive (6)/Customer_DF (1).csv")
print("Fraud Column Counts:\n", df_cust["Fraud"].value_counts())
