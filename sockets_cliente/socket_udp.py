import socket

# --- CONFIGURACIÓN ---
SERVER_IP = '192.168.1.XX'  # <--- CAMBIAR POR LA IP DE LA VM
PORT = 5000
# ---------------------

def run_tcp_client():
    # AF_INET = IPv4, SOCK_STREAM = TCP
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print(f"[*] Intentando conectar con el servidor en {SERVER_IP}:{PORT}...")
            s.connect((SERVER_IP, PORT))
            print("[+] Conexión establecida.")

            mensaje = input("Escribe tu nombre para el servidor TCP: ")
            s.sendall(mensaje.encode('utf-8'))

            # Recibir la respuesta del servidor
            data = s.recv(1024)
            print(f"[SERVIDOR]: {data.decode('utf-8')}")

    except ConnectionRefusedError:
        print("[!] Error: No se pudo conectar. Asegúrate de que el servidor esté corriendo.")
    except Exception as e:
        print(f"[!] Ocurrió un error: {e}")

if __name__ == "__main__":
    run_tcp_client()