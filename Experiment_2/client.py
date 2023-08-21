import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 4345)

while True:
    message = input("message from client\n")
    client_socket.sendto(message.encode(), server_address)
    data, server = client_socket.recvfrom(1024)
    print("Received:", data.decode())
    print()
# finally:
#     client_socket.close()
