# Questo script Python si connette a un database MySQL esistente e inserisce un nuovo record nella tabella 'customers'.
# 
# Funzionamento:
# 1. Importa il modulo 'mysql.connector' per interagire con un database MySQL.
# 2. Si stabilisce una connessione al database MySQL specificando:
#    - 'host="localhost"': il server del database si trova sulla stessa macchina (localhost).
#    - 'user="yourusername"': il nome utente per il login al database. Sostituire con le proprie credenziali.
#    - 'password="yourpassword"': la password per l'utente MySQL. Sostituire con la propria password.
#    - 'database="mydatabase"': il database a cui ci si connette, in questo caso 'mydatabase'. Assicurarsi che il database esista.
# 3. Una volta stabilita la connessione, viene creato un cursore (mycursor), che permette di eseguire le query SQL.
# 4. La variabile 'sql' contiene una query SQL che inserisce un nuovo record nella tabella 'customers', specificando
#    i valori per le colonne 'name' e 'address'. La query usa il segnaposto '%s' per evitare SQL injection e
#    permettere l'inserimento sicuro dei dati.
# 5. La variabile 'val' contiene i dati che devono essere inseriti nella tabella: il nome "John" e l'indirizzo "Highway 21".
# 6. La funzione 'mycursor.execute(sql, val)' esegue la query di inserimento, passando i valori 'val' come parametri.
# 7. Viene utilizzato 'mydb.commit()' per confermare la transazione e rendere permanente l'inserimento del record.
# 8. Alla fine, viene stampato il numero di righe inserite, utilizzando 'mycursor.rowcount', che restituirà il numero di 
#    record effettivamente inseriti nel database.
#
# Assicurati di sostituire 'yourusername' e 'yourpassword' con le tue credenziali MySQL e di avere il database 
# 'mydatabase' e la tabella 'customers' già creati prima di eseguire lo script.

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

# La query SQL per inserire un nuovo record nella tabella 'customers'
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")

# Eseguire la query di inserimento con i valori forniti
mycursor.execute(sql, val)

# Confermare la transazione per rendere permanente l'inserimento
mydb.commit()

# Stampare il numero di righe inserite
print(mycursor.rowcount, "record inserted.")
