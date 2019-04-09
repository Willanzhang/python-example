from socket import *

def main():
  #1. 创建套接字
  udpSocket = socket(AF_INET, SOCK_DGRAM)

  #2.bind
  udpSocket.bind(('', 8080))

  while True:
      recvInfo, ipInfo = udpSocket.recvfrom(1024)
      udpSocket.sendto(recvInfo, ipInfo)
      print(recvInfo.decode('gb2312'))


# from socket import *
# udp = socket(AF_INET, SOCK_DGRAM)
if __name__ == "__main__":
    main()