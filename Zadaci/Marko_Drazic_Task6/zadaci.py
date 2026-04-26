import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Markocrdrazic7@",
    database="movies_db"
)

cursor = conn.cursor()

cursor.execute("""
Select g.name AS genre, m.budget
FROM movie m
JOIN movie_genre mg ON m.movie_id = mg.movie_id
JOIN genre g ON mg.genre_id = g.genre_id
WHERE m.budget IS NOT NULL;
""")

result = cursor.fetchall()

print(result)

df = pd.DataFrame(result, columns=["genre", "budget"])

print(df.head())

avg_budget = df.groupby("genre")["budget"].mean()

print(avg_budget)
print(df.describe())