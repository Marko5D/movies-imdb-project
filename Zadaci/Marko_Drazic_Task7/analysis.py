import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

# Konekcija na MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Markocrdrazic7@",
    database="movies_db"
)

# SQL Upit
query = "SELECT budget, revenue FROM movie"

# Ucitavanje podataka u pandas
df = pd.read_sql(query, conn)
print(df.columns)

# Scatter plot
plt.scatter(df['budget'], df['revenue'])
plt.xlabel("Budget")
plt.ylabel("Revenue")
plt.title("Budget vs Revenue")
plt.savefig("budget_vs_revenue.png")
plt.show()

# Pearson korelacija
correlation = df[['budget, revenue']].corr().iloc[0, 1]
print(f"Korelacija izmedju budzeta i zarade: {correlation:.2f}")
