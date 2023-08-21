import socket
socketServer= socket.socket(socket.AF_INET ,socket.SOCK_DGRAM)
address=('localhost',4345)
socketServer.bind(address)
# print(socketServer)
print("Waiting and waiting and waiting and waiting.......")

while True: 
    # try:
    data,client_address=socketServer.recvfrom(2048)
    print("recieved",data.decode())
    response=input("hey TALK!!\n")
    socketServer.sendto(response.encode(),client_address)
    print()

