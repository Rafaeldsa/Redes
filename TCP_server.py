from socket import *

serverPort = int(input("Porta: "))
if serverPort > 1024: 
	
	HOST = 'localhost'
	PORT = serverPort
	udp = socket(AF_INET,SOCK_DGRAM)
	origem = (HOST, PORT)
	udp.bind(origem)
	
	print ("The server is ready to receive")

   
	while True:
        
        
		pair =  udp.recvfrom(1024)
		msg = pair[0]
		cliente = pair[1]
		msg = msg.decode().split(' ')   

		operation = msg[0].lower()
		val1 = float(msg[1])
		val2 = float(msg[2])

		result = 0
        
		if operation == "add":
			result = val1 + val2
		elif operation == "sub":  
			result = val1 - val2
		elif operation == "mult":
			result = val1 * val2
		elif operation == "div":
			result = (val1 * 1.0) / val2
		elif operation == "exp":
			result = (val1  * 1.0) ** val2
		else:
			result = -1

		result = str(result)
		print (result)
            
		udp.sendto(result.encode(), cliente)
else:
    print ("Impossible port")
