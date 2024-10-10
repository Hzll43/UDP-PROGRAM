import socket

def udp_server():
    server_ip = "0.0.0.0"  # Menerima dari semua antarmuka jaringan
    server_port = 8080    # Port yang digunakan oleh server

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((server_ip, server_port))

    print(f"Server UDP berjalan di {server_ip}:{server_port}...")

    try:
        while True:
            data, addr = sock.recvfrom(1024)  # Menerima data dari klien
            print(f"Message from {addr}: {data.decode('utf-8')}")
    except KeyboardInterrupt:
        print("Server stopped.")
    finally:
        sock.close()

if __name__ == "__main__":
    udp_server()
