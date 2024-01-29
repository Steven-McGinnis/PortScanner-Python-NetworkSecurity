import socket
from threading import Thread, Semaphore
import time

successful_ips = []

def check_ip(ip, port, sem):
    global successful_ips
    try:
        with socket.create_connection((ip, port), timeout=1) as sock:
            successful_ips.append(ip)
    except Exception:
        pass
    finally:
        sem.release()

def main():
    network_prefix = "192.168.0"
    port = 80 
    max_threads = 15
    sem = Semaphore(max_threads)

    for i in range(256):
        sem.acquire()  
        host_ip = f"{network_prefix}.{i}"
        t = Thread(target=check_ip, args=(host_ip, port, sem,))
        t.start()
        
        if i == 255:
            time.sleep(5)
            
    print("Successful IP addresses:")
    for ip in successful_ips:
        print(ip)

if __name__ == "__main__":
    main()
