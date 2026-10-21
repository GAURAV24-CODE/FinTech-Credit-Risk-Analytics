import pandas as pd

# UCI German Credit dataset
file_path = "data/raw/german.data"

# Column names based on the dataset struct
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

# Load raw data
df = pd.read_csv(
    file_path,
    sep=r"\s+",
    header=None,
    names=columns
)

print("=" * 60)
print("GERMAN CREDIT DATASET")
print("=" * 60)

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nCredit Risk Distribution:")
print(df["credit_risk"].value_counts())

print("\nBasic Statistics:")
print(df.describe(include="all").T)

print("=" * 60)