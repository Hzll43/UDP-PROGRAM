import socket

# Server IP address (set to '0.0.0.0' to accept connections from any IP)
server_ip = '0.0.0.0'  # Replace with the server's IP address
server_port = 8080

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP address and port
server_socket.bind((server_ip, server_port))

# Start listening for incoming connections
server_socket.listen(5)
print(f"Server listening on {server_ip}:{server_port}...")

while True:
    # Wait for a connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    # Receive data from client
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Received from client: {data}")
    
    # Send a response back to the client
    client_socket.send(b"Hello from server!")
    
    # Close the client socket
    client_socket.close()