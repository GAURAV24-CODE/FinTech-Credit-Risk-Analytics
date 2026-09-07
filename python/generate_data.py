import os
import numpy as np
import pandas as pd

# Reproducibility
np.random.seed(42)

# Number of records
N = 10000

# Create folders if they don't exist
os.makedirs("data/raw", exist_ok=True)

# -----------------------------
# 1. Customer & Loan IDs
# -----------------------------
customer_id = [f"CUST{i:05d}" for i in range(1, N + 1)]
loan_id = [f"LOAN{i:05d}" for i in range(1, N + 1)]

# -----------------------------
# 2. Borrower Information
# -----------------------------
age = np.random.randint(21, 66, N)

employment_type = np.random.choice(
    ["Salaried", "Self-employed", "Business", "Contract"],
    N,
    p=[0.50, 0.20, 0.20, 0.10]
)

annual_income = np.random.lognormal(
    mean=np.log(600000),
    sigma=0.45,
    size=N
).astype(int)

annual_income = np.clip(annual_income, 180000, 3000000)

credit_score = np.random.normal(700, 55, N).astype(int)
credit_score = np.clip(credit_score, 300, 850)

existing_loans = np.random.poisson(1.5, N)
existing_loans = np.clip(existing_loans, 0, 6)

# Debt-to-income ratio
dti_ratio = np.random.normal(0.35, 0.12, N)
dti_ratio = np.clip(dti_ratio, 0.05, 0.80)
dti_ratio = np.round(dti_ratio, 2)

# -----------------------------
# 3. Loan Information
# -----------------------------
loan_amount = np.random.lognormal(
    mean=np.log(350000),
    sigma=0.55,
    size=N
).astype(int)

loan_amount = np.clip(loan_amount, 50000, 1500000)

loan_term = np.random.choice(
    [12, 24, 36, 48, 60],
    N,
    p=[0.10, 0.20, 0.35, 0.20, 0.15]
)

loan_purpose = np.random.choice(
    [
        "Home Improvement",
        "Education",
        "Medical",
        "Business",
        "Debt Consolidation",
        "Personal"
    ],
    N,
    p=[0.15, 0.12, 0.10, 0.18, 0.25, 0.20]
)

application_channel = np.random.choice(
    ["Mobile App", "Website", "Branch", "Partner"],
    N,
    p=[0.40, 0.30, 0.20, 0.10]
)

region = np.random.choice(
    ["North", "South", "East", "West", "Central"],
    N
)

# -----------------------------
# 4. Application Dates
# -----------------------------
application_date = pd.date_range(
    start="2023-01-01",
    end="2025-12-31",
    periods=N
)

application_date = pd.to_datetime(application_date)

# -----------------------------
# 5. Approval Probability
# -----------------------------
approval_score = (
    0.55
    + (credit_score - 650) / 1000
    - dti_ratio * 0.30
    + np.minimum(existing_loans, 4) * (-0.025)
)

approval_probability = np.clip(
    approval_score,
    0.25,
    0.95
)

approval_random = np.random.random(N)

approval_status = np.where(
    approval_random < approval_probability,
    "Approved",
    "Rejected"
)

# -----------------------------
# 6. Interest Rate
# -----------------------------
interest_rate = (
    12
    + (700 - credit_score) * 0.025
    + dti_ratio * 8
    + np.random.normal(0, 1.2, N)
)

interest_rate = np.clip(
    interest_rate,
    7,
    25
)

interest_rate = np.round(interest_rate, 2)

# -----------------------------
# 7. Default Probability
# -----------------------------
risk_score = (
    0.04
    + np.maximum(0, 680 - credit_score) * 0.0012
    + np.maximum(0, dti_ratio - 0.35) * 0.65
    + np.maximum(0, existing_loans - 2) * 0.025
    + np.maximum(0, loan_amount / annual_income - 0.50) * 0.10
    + (loan_term >= 48) * 0.025
)

default_probability = np.clip(
    risk_score,
    0.01,
    0.45
)

default_random = np.random.random(N)

default_flag = np.where(
    (approval_status == "Approved") &
    (default_random < default_probability),
    1,
    0
)

# -----------------------------
# 8. Loan Status
# -----------------------------
loan_status = np.where(
    approval_status == "Rejected",
    "Rejected",
    np.where(
        default_flag == 1,
        "Default",
        np.random.choice(
            ["Active", "Closed"],
            N,
            p=[0.60, 0.40]
        )
    )
)

# -----------------------------
# 9. Create DataFrame
# -----------------------------
df = pd.DataFrame({
    "customer_id": customer_id,
    "loan_id": loan_id,
    "age": age,
    "employment_type": employment_type,
    "annual_income": annual_income,
    "credit_score": credit_score,
    "existing_loans": existing_loans,
    "dti_ratio": dti_ratio,
    "loan_amount": loan_amount,
    "loan_term": loan_term,
    "loan_purpose": loan_purpose,
    "application_channel": application_channel,
    "region": region,
    "application_date": application_date,
    "approval_status": approval_status,
    "interest_rate": interest_rate,
    "loan_status": loan_status,
    "default_flag": default_flag
})

# -----------------------------
# 10. Save Dataset
# -----------------------------
output_path = "data/raw/loan_applications.csv"

df.to_csv(output_path, index=False)

# -----------------------------
# 11. Display Summary
# -----------------------------
print("=" * 60)
print("FinTrust Lending - Synthetic Dataset Generated")
print("=" * 60)

print(f"Records created: {len(df):,}")
print(f"Columns created: {len(df.columns)}")
print(f"Saved to: {output_path}")

print("\nApproval Distribution:")
print(df["approval_status"].value_counts())

print("\nDefault Distribution:")
print(df["default_flag"].value_counts())

print("\nDefault Rate among approved loans:")

approved = df[df["approval_status"] == "Approved"]

if len(approved) > 0:
    default_rate = approved["default_flag"].mean() * 100
    print(f"{default_rate:.2f}%")

print("\nDataset Preview:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("=" * 60)