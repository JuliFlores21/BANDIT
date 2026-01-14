import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route('/search')
def search():
    # VULNERABILIDAD DAST (SQL Injection): Entrada de usuario sin sanitizar
    user_query = request.args.get('id')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # SQL vulnerable
    query = f"SELECT * FROM users WHERE id = {user_query}"
    cursor.execute(query)
    
    # VULNERABILIDAD SAST (Command Injection): Uso de os.system
    # Bandit detectará esto como un riesgo alto
    os.system(f"echo Buscando al usuario {user_query}")
    
    return f"Resultado para {user_query}"

if __name__ == "__main__":
    # VULNERABILIDAD SAST (Debug Mode): Nunca debe estar en True en producción
    app.run(debug=True, host='0.0.0.0', port=5000)