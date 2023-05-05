# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)


# importacao das bibliotecas
from socket import *  # sockets

# definicao das variaveis
serverName = 'localhost'  # ip do servidor a se conectar
serverPort = 61000  # porta a se conectar
clientSocket = socket(AF_INET, SOCK_DGRAM)  # criacao do socket UDP

message = input('Comando: ')
clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))  # envia mensagem para o servidor
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)  # recebe do servidor a resposta
print(f"O servidor ({serverName}, {serverPort}) respondeu com: {modifiedMessage.decode('utf-8')}")
clientSocket.close()  # encerra o socket do cliente