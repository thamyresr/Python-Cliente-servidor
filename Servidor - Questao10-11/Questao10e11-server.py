import socket, os

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
porta = 8881
socket_servidor.bind((host, porta))
socket_servidor.listen()
print("Servidor de nome", host, "esperando conexão na porta", porta)

while True:
    (socket_cliente, addr) = socket_servidor.accept()
    print("Conectado a:", str(addr))
    msg = socket_cliente.recv(4096)
    nome_arq = msg.decode('utf8')
    if os.path.isfile(nome_arq):
        tamanho = os.stat(nome_arq).st_size
        socket_cliente.send(str(tamanho).encode('utf8'))
        with open(nome_arq, 'rb') as arquivo:
            bytes = arquivo.read(4096)
            while bytes:
                socket_cliente.send(bytes)
                bytes = arquivo.read(4096)
        break;
    else:
        print("Não encontrou o arquivo")
        socket_cliente.send('-1'.encode('utf8'))

    socket_cliente.close()
socket_servidor.close()