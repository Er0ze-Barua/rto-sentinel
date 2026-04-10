from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
from data_prep import prepare_data


def train_rto_model():
    print("Fetching prepeared data...")
    X_train, X_Test, y_train, y_test = prepare_data()

    model = RandomForestClassifier(n_estimators=100, random_state=42)

    print("Training the random forest model")
    model.fit(X_train, y_train)

    predictions = model.predict(X_Test)
    print("\n----Model performance report----")
    print(classification_report(y_test, predictions))

    acc = accuracy_score(y_test, predictions)
    print(f"Final Accuracy: {acc *100:.2f}%")

    joblib.dump(model, "rto_model.pkl")
    print("\nModel saved as 'rto_model.pkl")


if __name__ == "__main__":
    train_rto_model()
