import socket
socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAddress = ("localhost", 4343)
socketServer.bind(serverAddress)
socketServer.listen(1)
print("w8ing")
socketClient, clientAddress = socketServer.accept()
print(socketClient, "client address", clientAddress)
while True:
    data = socketClient.recv(2048)
    print("rec:", data.decode())
    response = input("heyya")
    socketClient.sendall(response.encode())
    print()
