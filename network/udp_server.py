from socket import *
from time import ctime


HOST = ''
PORT = 5099
BUFSIZ = 4096
ADDRESS = (HOST, PORT)

def server():
    udpServerSocket = socket(AF_INET, SOCK_DGRAM)
    udpServerSocket.bind(ADDRESS)      # 绑定客户端口和地址

    while True:
        print("waiting for message...")
        print("\r\n------------------------------------------------\r\n")
        data, addr = udpServerSocket.recvfrom(BUFSIZ)
        print("接收到数据：", data.decode('utf-8'))

        content = '[%s] %s' % (bytes(ctime(), 'utf-8'), data.decode('utf-8'))
        udpServerSocket.sendto(content.encode('utf-8'), addr)
        print("\r\n------------------------------------------------\r\n")

if __name__ == '__main__':
    server()
