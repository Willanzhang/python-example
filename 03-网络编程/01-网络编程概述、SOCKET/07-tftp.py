from socket import *
import struct

udpSocket = socket(AF_INET, SOCK_DGRAM)
udpSocket.bind(('', 8080))

#组包
sendData = struct.pack("!H9sb5sb", 1, "down.html".encode(), 0, "octet".encode(), 0)

udpSocket.sendto(sendData, ('192.168.50.66', 69))

# 解包用unpack


while True:
    recvData,serverInfo = udpSocket.recvfrom(1024)

    cmdTuple = struct.unpack("!HH", recvData[:4])

    cmd = cmdTuple[0]
    packageNum = cmdTuple[1]

    if cmd == 3:
        if packageNum == 1:
            file = open('xx.html', 'w')
            file.write(recvData[4:].decode('utf-8'))
            # print(type(recvData[4:].decode('utf-8')))
        else:
            file.write(recvData[4:].decode('utf-8'))
        
        backData = struct.pack("!HH", 4, cmdTuple[1])
        udpSocket.sendto(backData, serverInfo)
    
    elif cmd == 5:
        print('ERROR')

    print(backData)

udpSocket.close()