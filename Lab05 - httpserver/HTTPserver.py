# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Base de um servidor HTTP (python 3)
#

# importacao das bibliotecas
import socket

# definicao do host e da porta do servidor
HOST = '' # ip do servidor (em branco)
PORT = 8080 # porta do servidor

# cria o socket com IPv4 (AF_INET) usando TCP (SOCK_STREAM)
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# permite que seja possivel reusar o endereco e porta do servidor caso seja encerrado incorretamente
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# vincula o socket com a porta (faz o "bind" do IP do servidor com a porta)
listen_socket.bind((HOST, PORT))

# "escuta" pedidos na porta do socket do servidor
listen_socket.listen(1)

# imprime que o servidor esta pronto para receber conexoes
print ('Serving HTTP on port %s ...' % PORT)

while True:
    # aguarda por novas conexoes
    client_connection, client_address = listen_socket.accept()
    # o metodo .recv recebe os dados enviados por um cliente atraves do socket
    request = client_connection.recv(1024)
    # troca o metodo de GET para POST para testar o erro 400
    request = request.replace(b'GET', b'POST', 1)
    # imprime na tela o que o cliente enviou ao servidor
    print (request.decode('utf-8'))
    request_split = (request.decode('utf-8').split(" "))
    if request_split[0] == "GET":
        if request_split[1] == "" or request_split[1] == "/":
            http_response = "HTTP/1.1 200 OK\r\n\r\n"
            with open('index.html', 'r', encoding='utf-8') as file:
                arquivo = file.read()
                http_response += arquivo
        else:
            caminho = request_split[1].split("/")
            try:
                with open(f'{caminho[1]}.html', 'r', encoding='utf-8') as file:
                    arquivo = file.read()
                    http_response = "HTTP/1.1 200 OK\r\n\r\n"
                    http_response += arquivo
            except FileNotFoundError:
                http_response = "HTTP/1.1 404 Not Found\r\n\r\n"
                with open('404.html', 'r', encoding='utf-8') as file:
                    arquivo = file.read()
                    http_response += arquivo
    else:
        http_response = "HTTP/1.1 400 Bad Request\r\n\r\n"
        with open('400.html', 'r', encoding='utf-8') as file:
            arquivo = file.read()
            http_response += arquivo
    # declaracao da resposta do servidor
    
    # servidor retorna o que foi solicitado pelo cliente (neste caso a resposta e generica)
    client_connection.send(http_response.encode('utf-8'))
    # encerra a conexao
    client_connection.close()

# encerra o socket do servidor
listen_socket.close()