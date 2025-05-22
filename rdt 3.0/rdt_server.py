import socket
import threading
import time
import utils

numero_seq = 0
HOST = 'localhost'
PORT = 5001

def heartbeat() -> None :
    while True:
        time.sleep(0.1)
        if numero_seq:
            pass

def start_server() -> None :                                                    
    heartbeatpeers = threading.Thread(target=heartbeat, args=(), daemon = True) # Uma thread comeca a resolver 
    heartbeatpeers.start()                                                      # Começa a thread
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)            # Conexão UDP
    server_socket.bind((HOST, PORT))                                            # Conexão no host 'localhost' e porta 5001
    print(f"[SERVIDOR] INICIADO EM: {HOST}:{PORT}")                      

    while True:
        """
         Maquina de estados do rdt 3.0
        """

        try:
            data, addr = server_socket.recvfrom(1024)  # Recebe dados do cliente
            print(f"[RECEBIDO] {data} de {addr}")

        except KeyboardInterrupt:
            print("[SERVIDOR] Encerrando.")
            break
        
    server_socket.close()

if __name__ == "__main__":
    start_server()         # INIT