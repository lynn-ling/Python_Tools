import socket
import sys
import time
def start_tcp_server(ip, port):
  print("start tcp server")
  #create socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_address = (ip, port)
  #bind port
  print('starting listen on ip %s, port %s'%server_address)
  sock.bind(server_address)
  #starting listening, allow only one connection
  try:
    sock.listen(1)
  except socket.error:
    print("fail to listen on port ")
    sys.exit(1)
  while True:
    time.sleep(10000)
    print ("waiting for connection")
    ##client,addr = sock.accept()
    print ('having a connection')
    ##client.close()


if __name__ == '__main__':
  start_tcp_server('127.0.0.1', 5001)