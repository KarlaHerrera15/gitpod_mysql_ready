# Questo script Python si connette a un database MySQL esistente e recupera tutti i record dalla tabella 'customers'.
# 
# Funzionamento:
# 1. Viene importato il modulo 'mysql.connector' che consente di interagire con il database MySQL.
# 2. Si stabilisce una connessione al database MySQL specificando:
#    - 'host="localhost"': il server del database si trova sulla stessa macchina (localhost).
#    - 'user="yourusername"': il nome utente per il login al database. Sostituire con le proprie credenziali.
#    - 'password="yourpassword"': la password per l'utente MySQL. Sostituire con la propria password.
#    - 'database="mydatabase"': il nome del database a cui ci si connette, in questo caso 'mydatabase'.
# 3. Una volta stabilita la connessione, viene creato un cursore (mycursor) che permette di eseguire le query SQL.
# 4. La query SQL 'SELECT * FROM customers' viene eseguita con 'mycursor.execute()', che recupera tutti i record 
#    dalla tabella 'customers'. Il simbolo '*' indica che vogliamo selezionare tutte le colonne.
# 5. La funzione 'mycursor.fetchall()' restituisce tutti i risultati della query in una lista di tuple. Ogni tupla 
#    rappresenta una riga della tabella con i suoi valori corrispondenti.
# 6. Un ciclo 'for' viene utilizzato per iterare su ogni riga del risultato e stampare ogni tupla.
# 7. Ogni iterazione del ciclo stampa i dati di un singolo record, rappresentato dalla tupla contenente i valori 
#    delle colonne 'name' e 'address' della tabella 'customers'.
#
# Assicurati di sostituire 'yourusername' e 'yourpassword' con le tue credenziali MySQL e di avere il database 
# 'mydatabase' e la tabella 'customers' già creati con dei dati inseriti prima di eseguire lo script.

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

# Eseguire la query per selezionare tutti i record dalla tabella 'customers'
mycursor.execute("SELECT * FROM customers")

# Recuperare tutti i risultati della query
myresult = mycursor.fetchall()

# Stampare ogni record (ogni tupla) nel risultato
for x in myresult:
  print(x)
