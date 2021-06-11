import socket

HOST = '127.0.0.1'
PORT = 8080
ADDRESS = (HOST,PORT)

ss = socket.socket()
ss.connect(ADDRESS)
ss.send(b'This is python')
res = (ss.recv(1024))
print(res)
ss.close()
