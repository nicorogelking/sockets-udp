import socket
import threading

def handle_tcp():
    # Socket TCP en puerto 6000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('0.0.0.0', 6000))
        s.listen(5)
        print("[TCP-EXP] Escuchando en puerto 6000...")
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"[TCP-EXP] Sesión iniciada desde {addr}")
                while True:
                    # Leemos en trozos pequeños de 1024 para demostrar segmentación
                    data = conn.recv(1024) 
                    if not data: break
                    print(f"[TCP-EXP] Fragmento recibido: {len(data)} bytes")

def handle_udp():
    # Socket UDP en el MISMO puerto 6000
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind(('0.0.0.0', 6000))
        print("[UDP-EXP] Escuchando en puerto 6000...")
        while True:
            # Buffer de 4096 para recibir datagramas completos > 1500 bytes
            data, addr = s.recvfrom(4096) 
            print(f"[UDP-EXP] Datagrama íntegro recibido: {len(data)} bytes desde {addr}")

# Lanzamos TCP en segundo plano
threading.Thread(target=handle_tcp, daemon=True).start()
# Lanzamos UDP en primer plano
handle_udp()