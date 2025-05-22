import socket
import time
import utils


HOST = 'localhost'
PORT = 5001
mensagem = "ola"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                        # Conexão UDP
s.sendto(mensagem.encode(), (HOST, PORT))                       # Conexão no host 'localhost' e porta 5001
#resposta, endereco_servidor = s.recvfrom(4096)
#print("Resposta:", resposta.decode())
#s.close()