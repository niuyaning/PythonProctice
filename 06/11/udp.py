import socket
import threading

def send_msg(udp_socket,dest_ip,dest_port):
    while True:
        send_data = input("请输入您要发送的消息")
        if send_data == "exit":
            break
        udp_socket.sendto(send_data.encode('gbk'),(dest_ip,dest_port))

def recv_msg(udp_socket):
    while True:
        recv_data,ip_port = udp_socket.recvform(1024)
        recv_content = recv_data.decode("gbk")
        print(">>>%s:%s" % (str(ip_port),recv_content))

if __name__ == '__main__':
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.bind("",8081)

    recv_thead = threading.Thread(target=recv_msg,args=(udp_socket))
    recv_thead.setDaemon(True)
    recv_thead.start()

    dest_ip = input("请输入对方的ip地址：")
    dest_port = input("请输入对方的端口号：")

    send_msg(udp_socket,dest_ip,dest_port)
    udp_socket.close()

