from socket import *
import threading
import sys

def handle_client(connectionSocket):
    try:
        # Receive the request message from the client
        message = connectionSocket.recv(1024).decode()
        if not message:
            connectionSocket.close()
            return

        # Extract the filename from the request
        filename = message.split()[1]
        
        # Open the requested file (skip the leading '/')
        f = open(filename[1:])
        outputdata = f.read()

        # Send HTTP Header
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        connectionSocket.send("\r\n".encode())

        # Send the content of the requested file
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()

    except IOError:
        # Send 404 Not Found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        connectionSocket.close()
    
    except Exception as e:
        print(f"Error handling request: {e}")
        connectionSocket.close()

def main():
    serverPort = 6789
    serverSocket = socket(AF_INET, SOCK_STREAM)
    
    # Bind and Listen
    serverSocket.bind(('', serverPort))
    serverSocket.listen(5) # Allow a backlog of 5 connections
    
    print(f"Multithreaded server is running on port {serverPort}...")

    try:
        while True:
            # Accept a new connection
            connectionSocket, addr = serverSocket.accept()
            print(f"Accepted connection from {addr}")

            # Create a new thread to handle this specific request
            client_thread = threading.Thread(target=handle_client, args=(connectionSocket,))
            client_thread.start()
            
    except KeyboardInterrupt:
        print("\nShutting down server...")
        serverSocket.close()
        sys.exit()

if __name__ == "__main__":
    main()