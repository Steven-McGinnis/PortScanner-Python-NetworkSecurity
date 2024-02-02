## Author: Steven McGinnis
## Date: 2/1/2024
## Email: stevenm1@muskingum.edu
## Purpose: This program is designed to scan a given IP address for open ports. It uses a multi-threaded approach to check the status of each port and prints the successful ports.
import socket
from threading import Thread, Semaphore
import time

import socket

def check_port(ip, port, sem, successful_ports):
    """
    Check if a specific port is open on a given IP address.

    Args:
        ip (str): The IP address to check.
        port (int): The port number to check.
        sem (Semaphore): A semaphore object for synchronization.
        successful_ports (list): A list to store the successful ports.

    Returns:
        None
    """
    try:
        with socket.create_connection((ip, port), timeout=1) as sock:
            successful_ports.append(port)
            sock.close()
            print(f"{port} Successfully Identified")
    except Exception:
        print(f"Port {port} Not Open")
    finally:
        sem.release()

def main():
    """
    This function performs port scanning on a given host IP address.
    It uses multiple threads to check the status of each port and prints the successful ports.
    """
    
    host_ip = "192.168.0.100"
    max_threads = 100
    sem = Semaphore(max_threads)
    successful_ports = []
    threads = []

    for port in range(1, 7001):
        sem.acquire()
        t = Thread(target=check_port, args=(host_ip, port, sem, successful_ports))
        t.start()
        threads.append(t)
        
    for t in threads:
        t.join()
        
    print_ports(successful_ports)
        
def print_ports(successful_ports):
    """
    Prints the list of successful ports.
    
    Args:
        successful_ports (list): A list of successful ports.
    
    Returns:
        None
    """
    if len(successful_ports) == 0:
        print("No successful ports found")
        return
    
    print("Successful ports:")
    sorted_ports = sorted(successful_ports)
    for port in sorted_ports:
        print(port)

def showStart():
    """
    Prints a message indicating the start of the port scan.
    """
    print("Starting Port Scan")

if __name__ == "__main__":
    """
    Namespace isolation for the main function. Not necessary, but good practice. 
    """
    showStart()
    main()
