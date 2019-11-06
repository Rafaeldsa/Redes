from socket import *

serverName = "localhost"
serverPort = int(input("Porta: "))
if serverPort > 1024: 
    HOST = 'localhost'
    PORT = serverPort
    udpSocket = socket(AF_INET,SOCK_DGRAM)
    destino = (HOST,PORT)
    udpSocket.connect(destino)
      
    sentence = input('Calculo: ')
    udpSocket.sendto(str.encode(sentence), destino)

    modifiedSentence = udpSocket.recvfrom(1024)

    print("Resultado:", modifiedSentence[0].decode())

else:
    print ("Impossible port")
