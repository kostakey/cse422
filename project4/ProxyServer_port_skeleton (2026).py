import socket
import ssl
import os
import threading

# Define the host and port for the proxy server
PROXY_HOST = '35.9.34.151'
PROXY_PORT = 8888

# List to store active client connections for clean-up
active_connections = []

def handle_client(client_socket):
    # Add client socket to active connections
    active_connections.append(client_socket)
    
    # Receive the client's request
    try:
        request = client_socket.recv(4096).decode()
        
        # Parse the requested URL from the client's request
        try:
            # Example: http://127.0.0.1:8888/www.bbc.com
            url = request.split()[1]
            hostname = url.split("/")[-1]
            print(f"hostname: {hostname}")
        except IndexError:
            print("Invalid request format.")
            client_socket.close()
            return
        
        # Define the cache file name based on the hostname
        cache_file = f"cache_{hostname}.html"
        
        # Check if the content is already cached
        if os.path.exists(cache_file):      
            # Read cached data and send it to the client
            
            with open(cache_file, "rb") as f:
                cached_data = f.read()
                client_socket.sendall(cached_data)

            ###############################
            # YOUR CODE IS HERE 
            ###############################
            
            print('\n**************************************************')
            print('**   DATA FROM CACHE')
            print('**************************************************\n')
                
        else:
            # Cache miss, fetch from the remote HTTPS server
            print(f"Cache miss for {hostname}, fetching from server...")

            # Establish an HTTPS connection to the target server
            context = ssl.create_default_context()
            with socket.create_connection((hostname, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    # Formulate the HTTPS GET request
                    get_request = f"GET / HTTP/1.1\r\nHost: {hostname}\r\nConnection: close\r\n\r\n"
                    ssock.sendall(get_request.encode())
                    
                    # Receive the response from the server and save it
                    
                    response = b""
                    while True:
                        data = ssock.recv(4096)
                        if not data:
                            break
                        response += data

                    ###############################
                    # YOUR CODE IS HERE
                    ###############################

            # Cache the received content
            
            with open(cache_file, "wb") as f:
                f.write(response)

            ###############################
            # YOUR CODE IS HERE 
            ###############################
            
            
            # Send the response to the client
            
            client_socket.sendall(response)

            ###############################
            # YOUR CODE IS HERE 
            ###############################
            
            print('\n**************************************************')
            print('**   DATA FROM ORIGINAL SERVER')
            print('**************************************************\n')
        

    finally:
        # Remove client socket from active connections and close it
        active_connections.remove(client_socket)
        client_socket.close()

# Main function to set up the proxy server
def start_proxy():
    # Create a socket for the proxy server
    proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_socket.bind((PROXY_HOST, PROXY_PORT))
    proxy_socket.listen(5)
    print(f"Proxy server is running on {PROXY_HOST}:{PROXY_PORT}...")

    try:
        while True:
            # Accept an incoming client connection
            client_socket, addr = proxy_socket.accept()
            print(f"Received connection from {addr}")
            
            # Handle the client request in a new thread
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()

    except KeyboardInterrupt:
        print("\nKeyboardInterrupt detected. Shutting down server...")

    finally:
        # Close the proxy socket
        proxy_socket.close()
        print("Proxy socket closed.")
        
        # Close all active client connections
        for conn in active_connections:
            try:
                conn.close()
                print("Closed an active client connection.")
            except Exception as e:
                print(f"Error closing client connection: {e}")

# Start the proxy server
if __name__ == "__main__":
    start_proxy()

