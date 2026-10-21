import os
import pandas as pd

# ------------------------
# File paths
# -----------------------------
input_file = "data/raw/german.data"
output_file = "data/processed/german_credit_clean.csv"

os.makedirs("data/processed", exist_ok=True)

# -----------------------------
# Column names
# -----------------------------
columns = [
    "checking_account",
    "duration_months",
    "credit_history",
    "purpose",
    "credit_amount",
    "savings_account",
    "employment_since",
    "installment_rate",
    "personal_status_sex",
    "other_debtors",
    "residence_since",
    "property",
    "age",
    "other_installment_plans",
    "housing",
    "existing_credits",
    "job",
    "dependents",
    "telephone",
    "foreign_worker",
    "credit_risk"
]

# -----------------------------
# Load raw data
# -----------------------------
df = pd.read_csv(
    input_file,
    sep=r"\s+",
    header=None,
    names=columns
)

print("=" * 60)
print("DATA CLEANING STARTED")
print("=" * 60)

print(f"Original rows: {len(df)}")
print(f"Original columns: {len(df.columns)}")

# -----------------------------
# Remove duplicates
# -----------------------------
duplicates = df.duplicated().sum()

print(f"Duplicate rows found: {duplicates}")

df = df.drop_duplicates()

# -----------------------------
# Check missing values
# -----------------------------
missing_values = df.isnull().sum().sum()

print(f"Missing values found: {missing_values}")

# -----------------------------
# Convert credit risk
# -----------------------------
# UCI dataset:
# 1 = Good credit risk
# 2 = Bad credit risk

df["credit_risk"] = df["credit_risk"].map({
    1: "Good",
    2: "Bad"
})

# Create numerical target for analysis
df["bad_credit_flag"] = df["credit_risk"].map({
    "Good": 0,
    "Bad": 1
})

# -----------------------------
# Feature engineering
# -----------------------------

# Age groups
df["age_group"] = pd.cut(
    df["age"],
    bins=[0, 25, 35, 50, 100],
    labels=["18-25", "26-35", "36-50", "51+"]
)

# Loan duration groups
df["loan_duration_group"] = pd.cut(
    df["duration_months"],
    bins=[0, 12, 24, 36, 100],
    labels=["<=12 months", "13-24 months", "25-36 months", "37+ months"]
)

# Credit amount groups
df["credit_amount_group"] = pd.cut(
    df["credit_amount"],
    bins=[0, 2500, 5000, 10000, float("inf")],
    labels=["Low", "Medium", "High", "Very High"]
)

# -----------------------------
# Data validation
# -----------------------------
print("\nData Validation:")

print("Negative credit amounts:",
      (df["credit_amount"] < 0).sum())

print("Invalid ages:",
      ((df["age"] < 18) | (df["age"] > 100)).sum())

print("Invalid durations:",
      (df["duration_months"] <= 0).sum())

print("Bad credit records:",
      df["bad_credit_flag"].sum())

# -----------------------------
# Save cleaned dataset
# -----------------------------
df.to_csv(output_file, index=False)

print("\n" + "=" * 60)
print("DATA CLEANING COMPLETED")
print("=" * 60)

print(f"Final rows: {len(df)}")
print(f"Final columns: {len(df.columns)}")
print(f"Saved to: {output_file}")

print("\nCredit Risk Distribution:")
print(df["credit_risk"].value_counts())

print("\nBad Credit Rate:")
print(
    f"{df['bad_credit_flag'].mean() * 100:.2f}%"
)

print("\nClean Dataset Preview:")
print(df.head())

print("=" * 60)