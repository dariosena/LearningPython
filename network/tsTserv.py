from socket import *
from time import ctime

HOST = ''
PORT = 21564
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection ...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('... connected from: '.format(addr))
    
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
            
        tcpCliSock.send(
            '[{0}] {1}'.format(bytes(ctime(), 'utf-8'), data).encode('utf-8'))
        
    tcpCliSock.close()

tcpSerSock.close()
