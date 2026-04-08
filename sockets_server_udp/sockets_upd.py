import socket

# Configuración del servidor
IP = '0.0.0.0'
PORT = 5001

def start_udp_server():
    # Crear socket: AF_INET (IPv4), SOCK_DGRAM (UDP)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((IP, PORT))
        print(f"[*] Servidor UDP iniciado en {IP}:{PORT}")
        print("[*] Escuchando datagramas de estudiantes...")

        while True:
            # Recibir datos y la dirección del remitente (crucial en UDP)
            data, addr = s.recvfrom(1024)
            
            mensaje = data.decode('utf-8')
            print(f"[UDP-DATA] Datagrama de {addr}: {mensaje}")
            
            # Responder al remitente
            respuesta = f"Servidor UDP: Recibido tu mensaje '{mensaje}'".encode('utf-8')
            s.sendto(respuesta, addr)
            print(f"[#] Respuesta UDP enviada a {addr}.")

if __name__ == "__main__":
    start_udp_server()