from socket import *
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python 3_YourLastName_webclient_multithread.py <host> <port> <file>")
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
    filename = sys.argv[3]

    try:
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((host, port))

        # GET request
        header = f"GET /{filename} HTTP/1.1\r\nHost: {host}\r\n\r\n"
        clientSocket.send(header.encode())

        # Buffer
        response = b""
        while True:
            data = clientSocket.recv(1024)
            if not data: break
            response += data

        print(response.decode())
        clientSocket.close()

    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    main()