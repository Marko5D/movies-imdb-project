import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Markocrdrazic7@",
    database="movies_db"
)

print("Konekcija uspesna!")