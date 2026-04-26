import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Markocrdrazic7@",
    database="movies_db"
)

cursor = conn.cursor()

cursor.execute("SHOW TABLES;")
tables = cursor.fetchall()

print("Tabele u bazi:")
for table in tables:
    print(table[0])

cursor.close()
conn.close()