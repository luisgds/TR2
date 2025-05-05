from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
while True :
    sentence = input("Digite uma frase para enviar via TCP: ")
    clientSocket.send(sentence.encode())
    response = clientSocket.recv(1024)
    print("Resposta do servidor:", response.decode())
clientSocket.close()
