import socket
socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveraddress = ("localhost", 4343)
socketClient.connect(serveraddress)
try:
    while True:
        request = input("enter the data")
        socketClient.sendall(request.encode())
        response = socketClient.recv(2048)
        print("received", response.decode(), end="\n")
finally:
    socketClient.close()
