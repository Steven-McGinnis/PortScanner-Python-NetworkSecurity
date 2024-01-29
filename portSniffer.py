import socket
from threading import Thread, Semaphore
import time

successful_ports = []

def check_ip(ip, port, sem):
    global successful_ports
    try:
        with socket.create_connection((ip, port), timeout=1) as sock:
            successful_ports.append(port)
    except Exception:
        pass
    finally:
        sem.release()

def main():
    host_ip = "192.168.100"
    max_threads = 15
    sem = Semaphore(max_threads)

    for i in range(7000):
        sem.acquire()  
        t = Thread(target=check_ip, args=(host_ip, i, sem,))
        t.start()
        
        if i == 6999:
            time.sleep(5)
        
    print("Successful ports:")
    sorted_ports = sorted(successful_ports)
    for port in sorted_ports:
        print(port)


if __name__ == "__main__":
    main()
