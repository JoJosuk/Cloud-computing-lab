import socket
socketClient=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serveraddress=('DALAB04',12345)

try:
    while True:
        socketClient.sendto("Njn joel".encode(), serveraddress)
        response=socketClient.recv(2048)
        print("received",response.decode())
finally:
    socketClient.close()