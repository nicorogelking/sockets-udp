import socket
import threading

def handle_tcp():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('0.0.0.0', 6000))
        s.listen(5)
        print("[TCP-EXP] Escuchando en puerto 6000...")
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"\n[TCP] Nueva conexión desde {addr}")
                total_recibido = 0
                operaciones = 0
                while True:
                    # Leemos de a 1024 bytes (menor al MTU de 1500)
                    # Esto forzará múltiples lecturas si el mensaje es grande
                    data = conn.recv(1024) 
                    if not data: break
                    
                    operaciones += 1
                    total_recibido += len(data)
                    print(f"  -> Lectura #{operaciones}: Recibidos {len(data)} bytes.")
                    print(f"  -> Total acumulado: {total_recibido} bytes.")

def handle_udp():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind(('0.0.0.0', 6000))
        print("[UDP-EXP] Escuchando en puerto 6000...")
        while True:
            # Buffer grande (4096) para recibir el datagrama completo
            data, addr = s.recvfrom(4096) 
            print(f"\n[UDP] Datagrama recibido desde {addr}")
            print(f"  -> Tamaño del mensaje: {len(data)} bytes (1 sola operación de lectura).")

threading.Thread(target=handle_tcp, daemon=True).start()
handle_udp()