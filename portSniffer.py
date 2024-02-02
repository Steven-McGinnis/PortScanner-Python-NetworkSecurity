import socket
from threading import Thread, Semaphore
import time

def check_port(ip, port, sem, successful_ports):
    try:
        with socket.create_connection((ip, port), timeout=5) as sock:
            successful_ports.append(port)
            sock.close()
            print(f"{port} Successfully Identified")
            
    finally:
        sem.release()

def main():
    host_ip = "192.168.0.100"
    max_threads = 20
    sem = Semaphore(max_threads)
    successful_ports = []
    threads = []

    for port in range(1, 2002):
        sem.acquire()
        t = Thread(target=check_port, args=(host_ip, port, sem, successful_ports))
        t.start()
        threads.append(t)
        
    for t in threads:
        t.join()
        
    print("Successful ports:")
    sorted_ports = sorted(successful_ports)
    for port in successful_ports:
        print(port)

def showStart():
    print("Starting Port Scan")

if __name__ == "__main__":
    showStart()
    main()
