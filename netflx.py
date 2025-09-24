import mysql.connector
import pandas as pd

# Connessione a MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="pythonuser",
    password="password123"
)
mycursor = mydb.cursor()

# Creazione del database NETFLIX_DB
mycursor.execute("CREATE DATABASE IF NOT EXISTS NETFLIX_DB")

# Usa il database NETFLIX_DB
mycursor.execute("USE NETFLIX_DB")

# Creazione della tabella Netflix_Shows
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS Netflix_Shows (
        show_id VARCHAR(20) PRIMARY KEY,
        type VARCHAR(20),
        title VARCHAR(255),
        director VARCHAR(255),
        cast TEXT,
        country VARCHAR(255),
        date_added VARCHAR(50),
        release_year INTEGER,
        rating VARCHAR(20),
        duration VARCHAR(50),
        listed_in VARCHAR(255),
        description TEXT
    );
""")

# Cancella dati dalla tabella (se presenti)
mycursor.execute("DELETE FROM Netflix_Shows")
mydb.commit()

# Lettura dati da CSV
netflix_data = pd.read_csv('./netflix_titles.csv')
netflix_data = netflix_data.fillna('Null')  # Riempie i valori NaN con 'Null'
print(netflix_data.head(10))

# Inserimento dati nella tabella
for i, row in netflix_data.iterrows():
    cursor = mydb.cursor()
    sql = """
    INSERT INTO Netflix_Shows 
    (show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    # Assicurati che l'ordine delle colonne di row corrisponda alla query
    cursor.execute(sql, (
        str(row['show_id']),
        row['type'],
        row['title'],
        row['director'],
        row['cast'],
        row['country'],
        row['date_added'],
        int(row['release_year']),
        row['rating'],
        row['duration'],
        row['listed_in'],
        row['description']
    ))
    mydb.commit()
    print(f"Record {row['show_id']} inserito")

# Controlla i dati inseriti
mycursor.execute("SELECT * FROM Netflix_Shows LIMIT 20")
myresult = mycursor.fetchall()

for record in myresult:
    print(record)