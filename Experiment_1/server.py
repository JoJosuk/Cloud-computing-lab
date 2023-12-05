import socket
socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('localhost', 4345)
socketServer.bind(address)
# print(socketServer)
socketServer.listen(1)
print("Waiting and waiting and waiting and waiting.......")
socketClient, client_address = socketServer.accept()
print(socketClient, client_address)
while True:
    # try:
    data = socketClient.recv(2048)
    print("recieved", data.decode())
    response = input("hey TALK!!\n")
    socketClient.sendall(response.encode())
    print()
