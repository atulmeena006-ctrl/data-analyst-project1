
SELECT COUNT(*) AS total_tickets
FROM support_tickets;

SELECT Category, COUNT(*) AS ticket_count
FROM support_tickets
GROUP BY Category
ORDER BY ticket_count DESC;

SELECT Priority, ROUND(AVG(Resolution_Hours), 2) AS avg_resolution_hours
FROM support_tickets
GROUP BY Priority
ORDER BY avg_resolution_hours DESC;
SELECT ROUND(
    100.0 * SUM(CASE WHEN SLA_Breached = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 2
) AS sla_breach_rate
FROM support_tickets;

SELECT Channel, ROUND(AVG(Customer_Satisfaction), 2) AS avg_satisfaction
FROM support_tickets
GROUP BY Channel
ORDER BY avg_satisfaction DESC;

SELECT Category, COUNT(*) AS sla_breaches
FROM support_tickets
WHERE SLA_Breached = 'Yes'
GROUP BY Category
ORDER BY sla_breaches DESC;
