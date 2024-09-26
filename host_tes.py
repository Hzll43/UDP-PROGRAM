import socket

# Server IP address (set to '0.0.0.0' to accept connections from any IP)
server_ip = '0.0.0.0'  
server_port = 8080    #adjust the port of the host and client

# Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

    sock.bind((server_ip, server_port))

    # Start listening for incoming connections
    sock.listen(5)
    print(f"Server listening on {server_ip}:{server_port}...")

    while True:
        # Wait for a connection
        client_socket, client_address = sock.accept()
        print(f"Connection established with {client_address}")

        # Receive data from client
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received from client: {data}")
    
        # Send a response back to the client
        client_socket.send(b"Hello from server!")
    
        # Close the client socket
        client_socket.close()
