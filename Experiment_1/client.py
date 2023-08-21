import socket
socketClient=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serveraddress=('localhost',4345)
socketClient.connect(serveraddress)

try:
    while True:
        request=input("hey SEND!!!\n")
        socketClient.sendall(request.encode())
        response=socketClient.recv(2048)
        print("received",response.decode())
        print()
finally:
    socketClient.close()