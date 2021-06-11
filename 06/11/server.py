import socket

HOST = '127.0.0.1'
PORT = 8080
ADDRESS = (HOST,PORT)

ss = socket.socket()
ss.bind(ADDRESS)
ss.listen()

while True:
    con,add = ss.accept()
    print("Server connected by",add)
    while True:
        data = con.recv(1024)
        if not data:
            break
        con.send(b'Echo=>' + data)
    con.close()