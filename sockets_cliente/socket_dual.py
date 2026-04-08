import socket
import time

SERVER_IP = 'LA_IP_DE_TU_VM' 
PUERTO = 6000
# Creamos un mensaje de 3000 bytes (relleno de letras 'A')
MENSAJE_GRANDE = b"A" * 3000 

def probar_diferencias():
    # --- PRUEBA UDP ---
    print(f"--- Enviando {len(MENSAJE_GRANDE)} bytes por UDP ---")
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s_udp:
        s_udp.sendto(MENSAJE_GRANDE, (SERVER_IP, PUERTO))
    
    time.sleep(2) # Pausa para ver los logs con calma
    
    # --- PRUEBA TCP ---
    print(f"--- Enviando {len(MENSAJE_GRANDE)} bytes por TCP ---")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_tcp:
        s_tcp.connect((SERVER_IP, PUERTO))
        s_tcp.sendall(MENSAJE_GRANDE)
        # Esperamos un poco para que el server procese antes de cerrar
        time.sleep(1) 

if __name__ == "__main__":
    probar_diferencias()