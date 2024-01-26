import socket
from threading import Thread

# Function to test a single IP address
def check_server(ip, port):
    try:
        with socket.create_connection((ip, port), timeout=1) as sock:
            print(f"Success: {ip}")
            sock.close()
    except Exception as e:
        print(f"Error: {ip} - {e}")

# Main script
def main():
    network_prefix = "192.X.X"  # Network prefix Replace X with your network prefix
    port = 80  # HTTP port

    for i in range(256):
        host_ip = f"{network_prefix}.{i}"
        t = Thread(target=check_server, args=(host_ip, port,))
        t.start()

if __name__ == "__main__":
    main()
