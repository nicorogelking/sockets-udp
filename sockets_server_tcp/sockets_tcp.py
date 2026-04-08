import socket

# Configuración del servidor
IP = '0.0.0.0'  # Escuchar en todas las interfaces de red de la VM
PORT = 5000

def start_tcp_server():
    # Crear socket: AF_INET (IPv4), SOCK_STREAM (TCP)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Reutilizar el puerto si se reinicia el script rápido
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        s.bind((IP, PORT))
        s.listen(5)
        print(f"[*] Servidor TCP iniciado en {IP}:{PORT}")
        print("[*] Esperando conexiones de estudiantes...")

        while True:
            # Aceptar conexión entrante
            conn, addr = s.accept()
            with conn:
                print(f"[+] Conexión establecida desde: {addr}")
                
                # Recibir datos (máximo 1024 bytes)
                data = conn.recv(1024)
                if not data:
                    break
                
                mensaje = data.decode('utf-8')
                print(f"[DATA] Mensaje recibido de {addr}: {mensaje}")
                
                # Enviar respuesta de confirmación
                respuesta = f"Servidor TCP: Hola {mensaje}, recibí tu mensaje correctamente.".encode('utf-8')
                conn.sendall(respuesta)
                print(f"[#] Respuesta enviada a {addr}. Cerrando conexión.")

if __name__ == "__main__":
    start_tcp_server()