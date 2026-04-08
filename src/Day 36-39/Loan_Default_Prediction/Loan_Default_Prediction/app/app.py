import joblib
import pandas as pd

# Load model
model = joblib.load("model/loan_model.pkl")

print("Loan Default Prediction")

# Load dataset to get feature names
df = pd.read_csv(r"B:/AIML Internship/src/Day 36-39/Loan_Default_Prediction.zip/Loan_Default_Prediction/data/loan_dataset_20000.csv")

# Remove target column
features = df.drop("loan_paid_back", axis=1).columns

# Take input for each feature
user_data = []

for feature in features:
    value = float(input(f"Enter {feature}: "))
    user_data.append(value)

# Convert input to DataFrame
input_df = pd.DataFrame([user_data], columns=features)

# Prediction
prediction = model.predict(input_df)

# Output
if prediction[0] == 1:
    print("Loan will be paid back (Safe)")
else:
    print("Loan may default (Risk)")