from socket import *
from thread import *
import threading
print_lock = threading.Lock()
serverSocket = socket(AF_INET, SOCK_STREAM)

def MultiThread(s):
        while True:
            try:
                message = s.recv(1024)
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata = f.read()
                s.send('HTTP/1.1 200 OK\r\n\r\n')
                for i in range(0, len(outputdata)):
                    s.send(outputdata[i]) 
                break
            except IOError:
                #Send response message for file not found
                s.send("HTTP/1.1 404 Not Found\r\n\r\n")
                s.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")
                #Fill in start
                #Fill in end
                #Close client socket
                break
        s.close()





def Main():
    #Prepare a sever socket
    #Fill in start
    serverSocket.bind(('localhost',1122))
    serverSocket.listen(5)
    #Fill in end
    while True:
        #Establish the connection
        print('Ready to serve...')
        connectionSocket, addr =  serverSocket.accept()
        print_lock.acquire() 
        start_new_thread(MultiThread, (connectionSocket,))
        print_lock.release()

    serverSocket.close()

if __name__ == '__main__': 
    Main() 