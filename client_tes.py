import socket

def udp_client():
    server_ip = "127.0.0.1"  # Alamat IP server (sesuaikan dengan alamat server)
    server_port = 12345      # Port server yang sesuai dengan yang digunakan oleh server

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print(f"Menghubungkan ke server UDP di {server_ip}:{server_port}...")

    while True:
        message = input("Masukkan pesan (ketik 'STOP' untuk berhenti): ")

        sock.sendto(message.encode('utf-8'), (server_ip, server_port))

        if message.strip().upper() == "STOP":
            print("Menghentikan client...")
            break

        data, addr = sock.recvfrom(1024)
        print(f"Pesan dari server: {data.decode('utf-8')}")

    sock.close()

if __name__ == "__main__":
    udp_client()
