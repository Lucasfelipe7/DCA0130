# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)


# importacao das bibliotecas
from socket import *  # sockets
import subprocess

# definicao das variaveis
serverName = ''  # ip do servidor (em branco)
serverPort = 61000  # porta a se conectar
serverSocket = socket(AF_INET, SOCK_STREAM)  # criacao do socket TCP
serverSocket.bind((serverName, serverPort))  # bind do ip do servidor com a porta
serverSocket.listen(1)  # socket pronto para 'ouvir' conexoes
print(f'Servidor TCP esperando conexoes na porta {serverPort}...')

while 1:
    connectionSocket, addr = serverSocket.accept()  # aceita as conexoes dos clientes
    comando = connectionSocket.recv(1024)  # recebe dados do cliente
    comando = comando.decode('utf-8')

    print(f'Cliente {addr} enviou: {comando}')
    comando = subprocess.check_output(
        comando, shell=True, universal_newlines=True, stderr=subprocess.STDOUT
    )
    connectionSocket.send(comando.encode('utf-8'))  # envia para o cliente
    connectionSocket.close()  # encerra o socket com o cliente
serverSocket.close()  # encerra o socket do servidor
