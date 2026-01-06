💳 Credit Card Fraud Detection System
📌 Project Overview

This project is a Machine Learning–based Credit Card Fraud Detection System that identifies whether a transaction is fraudulent or legitimate.
A Random Forest classifier is trained on real transaction data and deployed using a Streamlit web application for interactive predictions.

📊 Dataset

Source: Kaggle – Credit Card Fraud Detection Dataset

Path: /kaggle/input/creditcardfraud/creditcard.csv

Records: 284,807 transactions

Features:

V1 – V28 (PCA-transformed features)

Amount (Transaction amount)

Target Variable:

Class

0 → Legitimate

1 → Fraudulent

Note: The dataset is highly imbalanced.

⚙️ Technologies Used

Programming Language: Python

Machine Learning: Scikit-learn

Web Framework: Streamlit

Data Processing: Pandas, NumPy

🧠 Machine Learning Model

Algorithm: Random Forest Classifier

Imbalance Handling: class_weight='balanced'

Feature Scaling: StandardScaler (for Amount)

Evaluation Metrics:

Accuracy

Precision

Recall

F1-Score
