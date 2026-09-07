SELECT
    COUNT(*) AS total_customers,
    SUM(credit_amount) AS total_credit_amount,
    ROUND(AVG(credit_amount), 2) AS average_credit_amount,
    ROUND(AVG(age), 2) AS average_age
FROM credit_risk;

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


SELECT
    loan_duration_group,
    COUNT(*) AS customers,
    SUM(bad_credit_flag) AS bad_credit_customers,
    ROUND(AVG(bad_credit_flag) * 100, 2) AS bad_credit_rate
FROM credit_risk
GROUP BY loan_duration_group
ORDER BY bad_credit_rate DESC;


SELECT
    purpose,
    COUNT(*) AS customers,
    SUM(bad_credit_flag) AS bad_credit_customers,
    ROUND(AVG(bad_credit_flag) * 100, 2) AS bad_credit_rate
FROM credit_risk
GROUP BY purpose
ORDER BY bad_credit_rate DESC;


SELECT
    credit_history,
    COUNT(*) AS customers,
    SUM(bad_credit_flag) AS bad_credit_customers,
    ROUND(AVG(bad_credit_flag) * 100, 2) AS bad_credit_rate
FROM credit_risk
GROUP BY credit_history
ORDER BY bad_credit_rate DESC;


SELECT
    age_group,
    COUNT(*) AS customers,
    SUM(bad_credit_flag) AS bad_credit_customers,
    ROUND(AVG(bad_credit_flag) * 100, 2) AS bad_credit_rate
FROM credit_risk
GROUP BY age_group
ORDER BY bad_credit_rate DESC;