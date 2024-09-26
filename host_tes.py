import socket

server_ip = '0.0.0.0'  # Server IP address (set to '0.0.0.0' to accept connections from any IP)
server_port = 8080    #adjust the port of the host and client

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP/IP socket
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

    sock.bind((server_ip, server_port))

    sock.listen(5)   # Start listening for incoming connections 
    print(f"Server listening on {server_ip}:{server_port}...")

    while True:
        # Wait for a connection
        client_socket, client_address = sock.accept()
        print(f"Connection established with {client_address}")

        # Receive data from client
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received from client: {data}")
    
        client_socket.send(b"Hello from server!")  # Send a response back to the client
    
        client_socket.close()     # Close the client socket
