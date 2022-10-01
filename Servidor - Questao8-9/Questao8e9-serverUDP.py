import socket, psutil, pickle

socket_UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
PORTA = 9991
socket_UDP.bind((host, PORTA))
print("Servidor de nome", host, "esperando conexão na porta", PORTA)

while True:
    (msg, client) = socket_UDP.recvfrom(1024)
    if msg.decode('utf8') == 'fim':
        break
    resposta = []
    info_disco = psutil.disk_usage(".")
    disco_total = round(info_disco.total / (1024 * 1024 * 1024), 2)
    disco_disponivel = round(info_disco.free / (1024 * 1024 * 1024), 2)
    resposta.append(disco_total)
    resposta.append(disco_disponivel)

    bytes_resp = pickle.dumps(resposta)

    socket_UDP.sendto(bytes_resp, client)

socket_UDP.close()