import socket
import config_client

socket = socket.socket()
socket.connect(("localhost", 54610))

file = open(config_client.PATH_TO_FILE, "rb")
stream = file.read(65536)

while stream:
    socket.send(stream)
    stream = file.read(65536) # tried with 1024, 2048
socket.close()