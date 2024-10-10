import socket

def udp_receiver():
    server_ip = "0.0.0.0"  # Accept data from any network interface
    server_port = 8080      # Port to listen on

    # Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((server_ip, server_port))

    print(f"UDP receiver running on {server_ip}:{server_port}...")

    try:
        while True:
            # Receive data from any client (buffer size is 1024 bytes)
            data, addr = sock.recvfrom(1024)  
            print(f"Received message from {addr}: {data.decode('utf-8')}")
    except KeyboardInterrupt:
        print("Receiver stopped.")
    finally:
        sock.close()

if _name_ == "_main_":
    udp_receiver()
