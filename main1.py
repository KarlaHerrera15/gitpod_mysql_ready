# Questo script Python si connette a un database MySQL locale e crea un nuovo database.
# 
# Funzionamento:
# 1. Importa il modulo 'mysql.connector' che permette la comunicazione con MySQL.
# 2. Si stabilisce una connessione con il database MySQL attraverso il metodo 'mysql.connector.connect'.
#    - 'host="localhost"': il server del database si trova sulla stessa macchina (localhost).
#    - 'user="yourusername"': sostituire con il nome utente per il login al database.
#    - 'password="yourpassword"': sostituire con la password dell'utente MySQL.
# 3. Una volta connesso al database, viene creato un oggetto cursore (mycursor) che consente l'esecuzione di query SQL.
# 4. Viene eseguita la query SQL 'CREATE DATABASE mydatabase', che crea un nuovo database chiamato 'mydatabase'.
#
# Assicurati di sostituire 'yourusername' e 'yourpassword' con le tue credenziali MySQL prima di eseguire il codice.

import mysql.connector

# Stabilire la connessione con MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",    # Sostituire con il nome utente MySQL
  password="password123" # Sostituire con la password MySQL
)

# Creare un cursore per eseguire le query
mycursor = mydb.cursor()

# Eseguire la query per creare il database
mycursor.execute("CREATE DATABASE mydatabase")
