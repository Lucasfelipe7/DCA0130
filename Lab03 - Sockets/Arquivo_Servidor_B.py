# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)


# importacao das bibliotecas
from socket import *  # sockets

# definicao das variaveis
serverName = ''  # ip do servidor (em branco)
serverPort = 61000  # porta a se conectar
serverSocket = socket(AF_INET, SOCK_STREAM)  # criacao do socket TCP
serverSocket.bind((serverName, serverPort))  # bind do ip do servidor com a porta
serverSocket.listen(1)  # socket pronto para 'ouvir' conexoes
print(f'Servidor TCP esperando conexoes na porta {serverPort} ...')
while 1:
    connectionSocket, addr = serverSocket.accept()  # aceita as conexoes dos clientes
    sentence = connectionSocket.recv(1024)  # recebe dados do cliente
    sentence = sentence.decode('utf-8')
    sentence = sentence.replace(" ", "")

    if "obter" in sentence:
        sentence = sentence[5:]
        try:
            with open(sentence, "r") as arquivo:
                sentence = arquivo.read()
                print(f'Cliente {addr} enviou: {sentence}')
        except FileNotFoundError:
            sentence = "Arquivo nao encontrado"
            print(f'Cliente {addr} enviou: {sentence}')
    else:
        sentence = "Comando invalido"
        print(f'Cliente {addr} enviou: {sentence}')

    connectionSocket.send(sentence.encode('utf-8'))  # envia para o cliente
    connectionSocket.close()  # encerra o socket com o cliente
serverSocket.close()  # encerra o socket do servidor