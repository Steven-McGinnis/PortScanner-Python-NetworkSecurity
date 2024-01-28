import socket
import threading
from threading import Thread, Semaphore

# Function to test a single IP address
def check_ip(ip, port, sem):
    try:
        with socket.create_connection((ip, port), timeout=1) as sock:
            print(f"Success: {ip}")
    finally:
        sem.release()

# Main script
def main():
    network_prefix = "192.X.X"  # Network prefix Replace X with your network prefix
    port = 80  # HTTP port
    max_threads = 15
    sem = Semaphore(max_threads)

    for i in range(256):
        sem.acquire()  
        host_ip = f"{network_prefix}.{i}"
        t = Thread(target=check_ip, args=(host_ip, port, sem,))
        t.start()

if __name__ == "__main__":
    main()
