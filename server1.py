from socket import *                                  
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
#Fill in start
serverSocket.bind(('localhost',8800))
serverSocket.listen(1)
#Fill in end
while True:
    #Establish the connection
    print 'Ready to serve...'
    connectionSocket, addr =  serverSocket.accept()     
    try:
        message = connectionSocket.recv(1024)  #buffer size           
        filename = message.split()[1]                 
        f = open(filename[1:])        #reads from second char becuase the first one is '/'                
        outputdata = f.read()                  
       #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n') # if file is found it sends this header first
       #Fill in end                
        #Send the content of the requested file to the client 
        for i in range(0, len(outputdata)):           
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")
       
        #Close client socket
        connectionSocket.close()
#Fill in end
serverSocket.close()
