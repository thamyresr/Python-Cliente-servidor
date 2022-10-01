import socket
import os

def imprimir_status(bytes, tam):
    kbytes = bytes/1024
    tam_bytes = tam/1024
    texto = 'Baixando... '
    texto = texto + '{:<.2f}'.format(kbytes) + ' KB '
    texto = texto + 'de ' + '{:<.2f}'.format(tam_bytes) + ' KB'
    print(texto)

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
nome_arquivo = input('Entre com o nome do arquivo: ')

try:
    socket_cliente.connect((socket.gethostname(), 8881))
    socket_cliente.send(nome_arquivo.encode('utf8'))
    mensagem = socket_cliente.recv(12)
    tamanho = int(mensagem.decode('utf8'))
    if tamanho >= 0:
        diretorio = os.path.dirname(os.path.abspath(__file__))
        with open(diretorio +'\\' + nome_arquivo, "wb") as arquivo:
            soma = 0
            bytes = socket_cliente.recv(4096)
            while bytes:
                arquivo.write(bytes)
                soma = soma + len(bytes)
                os.system('cls')
                imprimir_status(soma, tamanho)
                bytes = socket_cliente.recv(4096)
    else:
        print('Arquivo não encontrado no servidor!')
except socket.error as erro:
    print(str(erro))

socket_cliente.close()
input("Pressione qualquer tecla para sair...")