import sqlite3
import pandas as pd

database_file = "data/final/credit_risk.db"

connection = sqlite3.connect(database_file)

queries = {
    "Portfolio Overview": """
        SELECT
            COUNT(*) AS total_customers,
            SUM(credit_amount) AS total_credit_amount,
            ROUND(AVG(credit_amount), 2) AS average_credit_amount,
            ROUND(AVG(age), 2) AS average_age
        FROM credit_risk;
    """,

    "Credit Risk Distribution": """
        SELECT
            credit_risk,
            COUNT(*) AS customers,
            ROUND(
                COUNT(*) * 100.0 /
                (SELECT COUNT(*) FROM credit_risk),
                2
            ) AS percentage
        FROM credit_risk
        GROUP BY credit_risk;
    """,

    "Risk by Loan Duration": """
        SELECT
            loan_duration_group,
            COUNT(*) AS customers,
            SUM(bad_credit_flag) AS bad_credit_customers,
            ROUND(AVG(bad_credit_flag) * 100, 2) AS bad_credit_rate
        FROM credit_risk
        GROUP BY loan_duration_group
        ORDER BY bad_credit_rate DESC;
    """,

    "Risk by Loan Purpose": """
        SELECT
            purpose,
            COUNT(*) AS customers,
            SUM(bad_credit_flag) AS bad_credit_customers,
            ROUND(AVG(bad_credit_flag) * 100, 2) AS bad_credit_rate
        FROM credit_risk
        GROUP BY purpose
        ORDER BY bad_credit_rate DESC;
    """,

    "Risk by Credit History": """
        SELECT
            credit_history,
            COUNT(*) AS customers,
            SUM(bad_credit_flag) AS bad_credit_customers,
            ROUND(AVG(bad_credit_flag) * 100, 2) AS bad_credit_rate
        FROM credit_risk
        GROUP BY credit_history
        ORDER BY bad_credit_rate DESC;
    """,

    "Risk by Age Group": """
        SELECT
            age_group,
            COUNT(*) AS customers,
            SUM(bad_credit_flag) AS bad_credit_customers,
            ROUND(AVG(bad_credit_flag) * 100, 2) AS bad_credit_rate
        FROM credit_risk
        GROUP BY age_group
        ORDER BY bad_credit_rate DESC;
    """
}

print("=" * 70)
print("FINTRUST CREDIT RISK - SQL ANALYSIS")
print("=" * 70)

for name, query in queries.items():

    print(f"\n\n### {name}")
    print("-" * 70)

    result = pd.read_sql_query(query, connection)

    print(result.to_string(index=False))

connection.close()

print("\n" + "=" * 70)
print("SQL ANALYSIS COMPLETED")
print("=" * 70)