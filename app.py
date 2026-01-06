import streamlit as st
import numpy as np
import pickle

# Load trained model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="centered"
)

st.title("💳 Credit Card Fraud Detection")
st.write("Enter transaction details to check whether it is **fraudulent or legitimate**.")

st.divider()

# Input fields for V1 to V28
st.subheader("Transaction Features")

features = []
for i in range(1, 29):
    value = st.number_input(
        f"V{i}",
        value=0.0,
        format="%.6f"
    )
    features.append(value)

# Amount input
amount = st.number_input(
    "Transaction Amount",
    min_value=0.0,
    value=0.0,
    format="%.2f"
)

# Predict button
if st.button("🔍 Predict"):
    try:
        # Scale amount
        amount_scaled = scaler.transform(np.array([[amount]]))[0][0]
        features.append(amount_scaled)

        # Convert to numpy array
        final_input = np.array(features).reshape(1, -1)

        # Prediction
        prediction = model.predict(final_input)[0]
        probability = model.predict_proba(final_input)[0][1]

        st.divider()

        if prediction == 1:
            st.error(f"🚨 Fraudulent Transaction\n\nProbability: {probability:.2%}")
        else:
            st.success(f"✅ Legitimate Transaction\n\nFraud Probability: {probability:.2%}")

    except Exception as e:
        st.warning("Please enter valid numeric values.")

