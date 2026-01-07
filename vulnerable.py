import os
import subprocess

# ERROR 1: Uso de shell=True (Vulnerabilidad de inyección de comandos)
def ping_server(ip):
    subprocess.call(f"ping -c 1 {ip}", shell=True)

# ERROR 2: Contraseña en duro (Hardcoded password)
db_password = "admin_password_123"

print("Escaneo completado")