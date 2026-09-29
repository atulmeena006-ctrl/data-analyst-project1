import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("customer_support_tickets.csv")
df["Created_Date"] = pd.to_datetime(df["Created_Date"])

# Data quality
print("===== DATA QUALITY =====")
print("Rows:", len(df))
print("Missing values:\n", df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

# KPIs
total_tickets = len(df)
average_resolution = df["Resolution_Hours"].mean()
sla_breach_rate = (df["SLA_Breached"] == "Yes").mean() * 100
average_satisfaction = df["Customer_Satisfaction"].mean()

print("\n===== KEY METRICS =====")
print("Total tickets:", total_tickets)
print(f"Average resolution: {average_resolution:.2f} hours")
print(f"SLA breach rate: {sla_breach_rate:.2f}%")
print(f"Average satisfaction: {average_satisfaction:.2f}/5")

# Category analysis
tickets_by_category = df["Category"].value_counts()
print("\n===== TICKETS BY CATEGORY =====")
print(tickets_by_category)

# Priority analysis
resolution_by_priority = df.groupby("Priority")["Resolution_Hours"].mean()
print("\n===== RESOLUTION BY PRIORITY =====")
print(resolution_by_priority.round(2))

# Channel analysis
satisfaction_by_channel = df.groupby("Channel")["Customer_Satisfaction"].mean()
print("\n===== SATISFACTION BY CHANNEL =====")
print(satisfaction_by_channel.round(2))

# Charts
tickets_by_category.plot(kind="bar", title="Tickets by Category")
plt.tight_layout()
plt.savefig("tickets_by_category.png")
plt.show()

resolution_by_priority.plot(kind="bar", title="Average Resolution Time by Priority")
plt.tight_layout()
plt.savefig("resolution_by_priority.png")
plt.show()

satisfaction_by_channel.plot(kind="bar", title="Average Customer Satisfaction by Channel")
plt.tight_layout()
plt.savefig("satisfaction_by_channel.png")
plt.show()
