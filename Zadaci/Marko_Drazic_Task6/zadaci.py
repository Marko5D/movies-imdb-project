import mysql.connector

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
JOIN movie_genre mg ON m.id = mg.movie_id
JOIN genre g ON mg.genre_id = g.id
WHERE m.budget IS NOT NULL;
""")

result = cursor.fetchall()

print(result)