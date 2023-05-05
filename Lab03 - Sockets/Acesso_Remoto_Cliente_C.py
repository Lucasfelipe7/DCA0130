# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)


# importacao das bibliotecas
from socket import *

# definicao das variaveis
serverName = 'localhost'  # ip do servidor
serverPort = 61000  # porta a se conectar
clientSocket = socket(AF_INET, SOCK_STREAM)  # criacao do socket TCP
clientSocket.connect((serverName, serverPort))  # conecta o socket ao servidor

comando = input('Insira o comando: ')
clientSocket.send(comando.encode('utf-8'))  # envia o texto para o servidor
modifiedComando = clientSocket.recv(1024)  # recebe do servidor a resposta
print(f"O servidor ({serverName}, {serverPort}) respondeu com: {modifiedComando.decode('utf-8')}")
clientSocket.close()  # encerramento o socket do cliente