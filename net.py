from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="pythonuser",
        password="password123",
        database="NETFLIX_DB"
    )

@app.route("/")
def home():
    return "🎬 Netflix Titles API"

@app.route("/all")
def get_all():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Netflix_Shows")  # <-- Tabella aggiornata
    columns = [col[0] for col in cursor.description]
    rows = cursor.fetchall()
    conn.close()
    return jsonify([dict(zip(columns, row)) for row in rows])

@app.route("/movies")
def get_movies():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Netflix_Shows WHERE Category = 'Movie'")  # <-- Tabella aggiornata
    columns = [col[0] for col in cursor.description]
    rows = cursor.fetchall()
    conn.close()
    return jsonify([dict(zip(columns, row)) for row in rows])

@app.route("/tvshows")
def get_tvshows():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Netflix_Shows WHERE Category = 'TV Show'")  # <-- Tabella aggiornata
    columns = [col[0] for col in cursor.description]
    rows = cursor.fetchall()
    conn.close()
    return jsonify([dict(zip(columns, row)) for row in rows])

@app.route("/country/Thailand")
def get_thailand():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM Netflix_Shows WHERE Country LIKE %s"
    cursor.execute(query, ('%Thailand%',))
    columns = [col[0] for col in cursor.description]
    rows = cursor.fetchall()
    conn.close()
    return jsonify([dict(zip(columns, row)) for row in rows])


@app.route("/year/2019")
def get_year_2019():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM Netflix_Shows WHERE Release_Date LIKE %s"
    # Poiché Release_Date è stringa tipo 'August 14, 2020', dobbiamo filtrare con LIKE '%2019%'
    cursor.execute(query, ('%2019%',))
    columns = [col[0] for col in cursor.description]
    rows = cursor.fetchall()
    conn.close()
    return jsonify([dict(zip(columns, row)) for row in rows])


if __name__ == "__main__":
    app.run(debug=True)
