import socket
import config_server

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 54610))
server.listen(5)

while True:
    inbound_stream, address = server.accept()

    print(address)
    counter = 1
    file = open(config_server.PATH_TO_FILE, 'wb')
    counter += 1
    while(True):
        stream = inbound_stream.recv(65536)
        while stream:
            file.write(stream)
            stream = inbound_stream.recv(65536)
        file.close()
        inbound_stream.close()

socket.close()
