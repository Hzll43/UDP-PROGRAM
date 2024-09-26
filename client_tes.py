import socket

# Server's IP address and port
server_ip = '192.168.99.150'  # Replace with the server's IP address
server_port = 8080

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
# Connect to the server
client_socket.connect((server_ip, server_port))
print(f"Connected to server at {server_ip}:{server_port}")

# Send a message to the server
client_socket.send(b"Start the Robot!")

# Receive response from the server
response = client_socket.recv(1024).decode('utf-8')
print(f"Received from server: {response}")

# Close the client socket
client_socket.close()
