# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)


# importacao das bibliotecas
from socket import *  # sockets
import time

# definicao das variaveis
serverName = ''  # ip do servidor (em branco)
serverPort = 61000  # porta a se conectar
serverSocket = socket(AF_INET, SOCK_DGRAM)  # criacao do socket UDP
serverSocket.bind((serverName, serverPort))  # bind do ip do servidor com a porta
print(f'Servidor UDP esperando conexoes na porta {serverPort} ...')

while 1:
    message, clientAddress = serverSocket.recvfrom(2048)  # recebe do cliente
    message = message.decode('utf-8')
    message = message.lower()

    if message == 'data':
        modifiedMessage = str(time.ctime())
    else:
        modifiedMessage = "Comando invalido"
    
    print(f'Cliente {clientAddress} enviou: {message}, transformando em: {modifiedMessage}')
    serverSocket.sendto(modifiedMessage.encode('utf-8'), clientAddress)  # envia a resposta para o cliente
serverSocket.close()  # encerra o socket do servidor