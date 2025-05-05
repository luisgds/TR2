from socket import *
import threading
clientes = {}
heartBeats = {}
heart = 20

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print('Servidor TCP aguardando conexão...')

def server(client_socket, addr):
    sentence = client_socket.recv(1024).decode()
    print(f"Cliente novo no server: {sentence}")
    response = "Você foi cadastrado no server"
    client_socket.send(response.encode())
    while True:
        sentence = client_socket.recv(1024).decode()
        print(f"Recebido: {sentence}")
        response = sentence.upper()
        client_socket.send(response.encode())
    client_socket.close()

while True:
    client_socket, addr = serverSocket.accept()
    thread = threading.Thread(target = server, args=(client_socket, addr))
    thread.start()

serverSocket.close()

