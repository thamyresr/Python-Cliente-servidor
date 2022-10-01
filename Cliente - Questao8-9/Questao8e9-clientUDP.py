import socket, pickle

PORTA = 9991

def imprime(l):
    texto = ''
    for i in l:
        texto = texto + ' {:>8.2f} '.format(i) + 'GB'
    print(texto)

socket_UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    socket_UDP.connect((socket.gethostname(), PORTA))
    msg = ' '
    print('{:>10}'.format('TOTAL')+'{:>15}'.format('DISPONÍVEL'))
    socket_UDP.send(msg.encode('utf8'))
    bytes = socket_UDP.recv(1024)
    lista = pickle.loads(bytes)
    imprime(lista)
    msg = 'fim'
    socket_UDP.send(msg.encode('utf8'))
except Exception as erro:
    print(str(erro))

socket_UDP.close()
input("Pressione qualquer tecla para sair...")