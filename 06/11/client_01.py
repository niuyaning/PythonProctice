import socket

HOST = '127.0.0.1'
PORT = 8080
ADDRESS = (HOST,PORT)

ss = socket.socket(type=socket.SOCK_DGRAM) #udp socket
ss.bind(ADDRESS)
msg,add = ss.recvfrom(1024)
print(msg)

ss.sendto(b'Hello',add)
ss.close()