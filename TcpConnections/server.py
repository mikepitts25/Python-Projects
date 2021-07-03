import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = socket.gethostname()
host = '192.168.235.1'
port = 4444

serversocket.bind((host, port))

serversocket.listen(1)

while True:
    clientsocket, address = serversocket.accept()

    print("Received connection from {0} ".format(address))

    message = "Hello. Thank you for connecting to the server.\r\n"
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()
