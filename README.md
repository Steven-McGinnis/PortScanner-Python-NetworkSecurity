# Port Sniffer 🛠️

This **Port Sniffer** is a Python-based program designed to scan a given IP address for open ports. It uses a multi-threaded approach to check the status of each port and prints the successful ports. Additionally, it saves the list of successful ports to a file.

---

## Features

- **Multi-threaded Scanning**:
  - Utilizes multiple threads to scan ports concurrently, improving scanning speed.
- **Port Status Checking**:
  - Checks if a specific port is open on a given IP address.
- **Result Logging**:
  - Prints the list of successful ports.
  - Saves the list of successful ports to a file.

---

## File Structure

- **`portSniffer.py`**: Contains the main program logic, including port scanning, result printing, and saving successful ports to a file.

---

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Steven-McGinnis/PortSniffer.git
   ```

2. **Navigate to the Directory**:

   ```bash
   cd PortSniffer
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Program**:

   ```bash
   python portSniffer.py
   ```

2. **Enter the IP Address**:

   - Enter the IP address you want to scan for open ports.

3. **View the Results**:

   - The program will display the list of successful ports and save them to a file.

---

---

## Limitations

- **Single Port per Host in Network Scans**:
  - During network scans, the tool checks only one port per IP (default: port 80). To customize, edit the `port` variable in the network scan section.
- **Timeout Duration**:

  - The default timeout for socket connections is 1 second. Adjust this in the `check_port()` or `check_ip()` functions if needed for slower networks.

- **Maximum Threads**:

  - The number of concurrent threads is capped at 100 for port scans and 15 for network scans by default. Increasing this may speed up scans but could also overwhelm system resources.

- **No Service Detection**:
  - The tool does not identify the services running on open ports. Only port status is provided.

---

## Future Enhancements

- **Service Identification**:
  - Integrate service identification for open ports (e.g., detecting if HTTP, FTP, or SSH is running).
- **Dynamic Network Scanning**:

  - Add functionality to automatically detect and scan the local subnet.

- **Graphical Output**:

  - Provide a user-friendly GUI to visualize scanning progress and results.

- **Output to File**:

  - Include built-in functionality to save results to a `.txt` or `.csv` file.

- **Cross-Platform Compatibility**:
  - Ensure full compatibility with Windows and macOS systems.

---

## Acknowledgments

This project was created as part of a hands-on learning experience in Python programming and network security. Special thanks to the instructor for providing guidance and inspiration for this project.

---

Feel free to fork and modify the project to fit your specific needs. Contributions are always welcome!
