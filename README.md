📊 FinTrust Lending — Credit Risk Analytics Platform

An end-to-end credit risk analytics project using Python, SQL, and Power BI to analyze borrower and loan characteristics associated observed credit risk.

📌 Project Overview

FinTrust Lending is a fictional digital lending company that wants to better understand its credit portfolio and identify borrower and loan characteristics associated with higher observed credit risk.

This project analyzes the UCI Statlog German Credit Data dataset to uncover patterns in credit risk, loan duration, credit history, loan purpose, borrower age, employment, and credit amount.

The analysis follows an end-to-end data analytics workflow:

Python → Data Cleaning → EDA → SQL → Power BI → Business Insight

🎯 Business 

A lending company needs to understand:

What percentage of customers have observed bad credit?
Which loan purposes have higher observed bad-credit rates?
How does loan duration relate to observed credit risk?
How does credit history relate to credit risk?
How does risk vary across borrower age groups?
What patterns can help management monitor portfolio risk?
Business Objective

The objective is to transform raw credit data into clear, decision-supporting insights that can help a lending business monitor portfolio risk.

Important: The analysis identifies associations in historical data. It does not establish causation or recommend automated lending decisions.

🗂️ Dataset

Dataset: UCI Statlog German Credit Data

Source: UCI Machine Learning Repository

1,000 credit records
20 original features
Binary credit-risk target
1 = Good Credit
2 = Bad Credit

The dataset is used for educational and portfolio-analysis purposes.

Citation:

Hofmann, H. (1994). Statlog (German Credit Data). UCI Machine Learning Repository. DOI: 10.24432/C5NC77.

🛠️ Tech Stack
Technology	Purpose
🐍 Python	Data loading, cleaning & EDA
🗄️ SQLite	SQL analysis & querying
📊 Power BI	Interactive dashboard
📓 Jupyter Notebook	Exploratory Data Analysis
🐙 GitHub	Version control & portfolio
📁 Pandas	Data manipulation
📈 Matplotlib / Seaborn	Data visualization
🔄 Project Workflow
Raw UCI Dataset
       ↓
Python Data Loading
       ↓
Data Cleaning & Validation
       ↓
Feature Engineering
       ↓
Exploratory Data Analysis
       ↓
SQLite Database
       ↓
SQL Analysis
       ↓
Power BI Dashboard
       ↓
Business Insights
🧹 Data Cleaning

The Python preprocessing pipeline performs:

Duplicate detection and removal
Missing-value validation
Credit-risk label transformation
Age-group creation
Loan-duration grouping
Credit-amount grouping
Basic data-quality validation
Output of a clean analytical dataset
Engineered Features
Feature	Description
bad_credit_flag	1 for Bad Credit, 0 for Good Credit
age_group	Age categories
loan_duration_group	Loan duration categories
credit_amount_group	Credit amount categories
🔍 Exploratory Data Analysis

The EDA investigates:

Credit Risk Distribution

Distribution of Good vs Bad credit customers.

Loan Duration

Comparison of observed bad-credit rates across loan-duration groups.

Loan Purpose

Identification of loan purposes with relatively higher observed risk.

Credit History

Analysis of observed risk across credit-history categories.

Age

Comparison of observed risk across age groups.

Employment

Analysis of observed risk across employment-duration categories.

Credit Amount

Distribution and comparison of credit amounts across risk groups.

🗄️ SQL Analysis

The cleaned dataset is loaded into a SQLite database.

Key SQL analyses include:
Overall portfolio statistics
Good vs Bad credit distribution
Bad-credit rate by loan duration
Bad-credit rate by loan purpose
Bad-credit rate by credit history
Bad-credit rate by age group

Example:

SELECT
    loan_duration_group,
    COUNT(*) AS total_customers,
    ROUND(AVG(bad_credit_flag) * 100, 2) AS bad_credit_rate
FROM credit_risk
GROUP BY loan_duration_group
ORDER BY bad_credit_rate DESC;
📊 Power BI Dashboard

The Power BI report contains three analytical pages.

1️⃣ Credit Risk Overview

Provides a high-level view of the credit portfolio.

KPIs
Total Customers
Total Credit Amount
Average Credit Amount
Bad Credit Rate
Visuals
Good vs Bad Credit
Risk by Loan Purpose
Risk by Loan Duration
2️⃣ Borrower & Loan Risk

Provides deeper borrower and loan-level analysis.

Visuals
Risk by Age Group
Risk by Credit History
Risk by Employment
Average Credit Amount by Risk
Loan Duration vs Credit Amount
3️⃣ Portfolio Insights

Provides management-focused portfolio observations.

Visuals
Highest Observed Risk by Loan Purpose
Observed Risk by Loan Duration
Observed Risk by Credit History
Key Business Insights
💡 Key Business Insights

Based on the analysis:

Longer loan-duration categories show differences in observed bad-credit rates.
Credit history shows a notable association with observed credit risk.
Risk levels vary across different loan purposes.
Borrower age and employment categories show differences in observed risk.
Credit amount and loan duration provide useful portfolio-segmentation dimensions.

These findings represent observed associations in the dataset, not causal relationships.

⚖️ Fairness & Responsible Use

Credit-risk analysis can introduce fairness and bias concerns.

For a real lending system:

Protected or sensitive characteristics should not be used as inappropriate approval criteria.
Model performance should be evaluated across relevant demographic groups.
Fairness and bias testing should be performed before deployment.
Historical patterns should not automatically be treated as valid decision rules.
Human oversight and regulatory requirements should be considered.

In particular, variables such as personal_status_sex and foreign_worker require careful treatment and should not simply be used as underwriting criteria.

📁 Project Structure
FinTech-Credit-Risk-Analytics/
│
├── data/
│   ├── raw/
│   │   └── german.data
│   │
│   ├── processed/
│   │   └── german_credit_clean.csv
│   │
│   └── final/
│       └── credit_risk.db
│
├── notebooks/
│   └── credit_risk_analysis.ipynb
│
├── python/
│   ├── load_data.py
│   ├── data_cleaning.py
│   ├── create_database.py
│   └── run_sql_analysis.py
│
├── sql/
│   └── credit_risk_analysis.sql
│
├── powerbi/
│   └── fintech.pbix
│
├── screenshots/
│   ├── credit_risk_overview.png
│   ├── borrower_loan_risk.png
│   └── portfolio_insights.png
│
├── docs/
│
├── tests/
│
├── .gitignore
└── README.md
🚀 How to Run the Project
1. Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL
cd FinTech-Credit-Risk-Analytics
2. Create a virtual environment
python -m venv .venv
3. Activate the environment
Windows
.venv\Scripts\activate
4. Install dependencies
pip install pandas numpy matplotlib seaborn jupyter
5. Run data loading
python python/load_data.py
6. Run data cleaning
python python/data_cleaning.py
7. Create the SQLite database
python python/create_database.py
8. Run SQL analysis
python python/run_sql_analysis.py
9. Open the Power BI report

Open:

powerbi/fintech.pbix
📸 Dashboard Preview

Add your three Power BI screenshots here:

## Dashboard Preview

### Credit Risk Overview

![Credit Risk Overview](screenshots/credit_risk_overview.png)

### Borrower & Loan Risk

![Borrower & Loan Risk](screenshots/borrower_loan_risk.png)

### Portfolio Insights

![Portfolio Insights](screenshots/portfolio_insights.png)
📈 Skills Demonstrated

This project demonstrates:

Data Cleaning
Data Validation
Exploratory Data Analysis
Feature Engineering
SQL Aggregations
SQL Grouping & Filtering
SQLite Database Management
Power BI Dashboard Development
DAX Measures
Business Intelligence
Data Storytelling
Portfolio Risk Analysis
Responsible/Fairness-aware Analytics
🎓 What I Learned

Through this project, I practiced:

Converting raw data into an analytical dataset
Building reusable Python data-cleaning workflows
Using SQL for business-oriented analysis
Designing interactive Power BI dashboards
Translating analytical findings into business insights
Communicating limitations and responsible-use considerations
⚠️ Limitations
The dataset contains only 1,000 observations.
The analysis is based on historical data.
Observed relationships do not imply causation.
The project does not build or deploy a production credit-scoring model.
Results should not be used directly for real-world lending decisions.
📚 Data Source

Hofmann, H. (1994). Statlog (German Credit Data). UCI Machine Learning Repository.

Dataset DOI: 10.24432/C5NC77

👨‍💻 Author

Gaurav Eknath Kumbhar

Aspiring Data Analyst | Python | SQL | Power BI
