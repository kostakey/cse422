from socket import *
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python 2_YourLastName_webclient.py server_host server_port filename")
        sys.exit()

    # Get command line arguments
    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]

    try:
        clientSocket = socket(AF_INET, SOCK_STREAM)

        clientSocket.connect((server_host, server_port))

        # GET request
        if not filename.startswith('/'):
            filename = '/' + filename
            
        request = f"GET {filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"

        # Send 
        clientSocket.send(request.encode())

        print(f"--- Requesting {filename} from {server_host}:{server_port} ---\n")
        
        response = b""
        while True:
            data = clientSocket.recv(1024)
            if not data:
                break
            response += data

        print(response.decode())

        clientSocket.close()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()