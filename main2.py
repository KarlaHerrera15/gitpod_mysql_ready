# Questo script Python si connette a un database MySQL esistente e crea una nuova tabella chiamata 'customers'.
# 
# Funzionamento:
# 1. Viene importato il modulo 'mysql.connector' che consente di interagire con un database MySQL.
# 2. Si stabilisce una connessione al database MySQL specificando:
#    - 'host="localhost"': il server del database si trova sulla stessa macchina (localhost).
#    - 'user="yourusername"': il nome utente per il login al database. Sostituire con le proprie credenziali.
#    - 'password="yourpassword"': la password per l'utente MySQL. Sostituire con la propria password.
#    - 'database="mydatabase"': specifica il database a cui ci si connette, in questo caso 'mydatabase'.
# 3. Una volta connessi al database, viene creato un cursore (mycursor), che permette di eseguire le query SQL.
# 4. Viene eseguita la query SQL 'CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))', 
#    che crea una tabella chiamata 'customers' con due colonne:
#    - 'name': una colonna di tipo VARCHAR che può contenere una stringa di massimo 255 caratteri.
#    - 'address': una colonna di tipo VARCHAR che può contenere una stringa di massimo 255 caratteri.
#
# Assicurati di sostituire 'yourusername' e 'yourpassword' con le tue credenziali e di avere il database 'mydatabase' 
# già creato prima di eseguire questo script.

import mysql.connector

# Stabilire la connessione con MySQL e selezionare il database 'mydatabase'
mydb = mysql.connector.connect(
  host="localhost",        # Server del database
  user="pythonuser",     # Nome utente MySQL
  password="password123", # Password MySQL
  database="mydatabase"    # Database a cui ci si connette
)

# Creare un cursore per eseguire le query
mycursor = mydb.cursor()

# Eseguire la query per creare la tabella 'customers'
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
