import sqlite3

# Conectar a la base de datos (se creará si no existe)
connection = sqlite3.connect('database.db')

# Crear la tabla 'users'
with open('schema.sql', 'w') as f:
    connection.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT);')

# Insertar un dato de prueba
cursor = connection.cursor()
cursor.execute("INSERT INTO users (id, name) VALUES (1, 'Usuario de Prueba')")

connection.commit()
connection.close()
print("Base de datos e información inicial creadas con éxito.")