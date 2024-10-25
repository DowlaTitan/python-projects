import socket
 # import requests
import re

# Function to scan for open ports
def scan_ports(target, port_range):
    open_ports = []
    for port in range(1, port_range + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

# Function to check software version (example using HTTP headers)
def check_software_version(target):
    try:
        response = requests.get(target)
        server = response.headers.get('Server', 'Unknown')
        version = re.search(r'\d+\.\d+', server)  # Simple regex to find version numbers
        return server if version else "No version found"
    except Exception as e:
        return f"Error: {e}"

# Main function
def main():
    target = input("Enter the target IP or website: ")
    port_range = int(input("Enter the port range to scan (e.g., 100): "))

    print(f"Scanning {target} for open ports...")
    open_ports = scan_ports(target, port_range)
    if open_ports:
        print(f"Open ports: {open_ports}")
    else:
        print("No open ports found.")

    if target.startswith("http://") or target.startswith("https://"):
        print(f"Checking software version for {target}...")
        software_version = check_software_version(target)
        print(f"Server information: {software_version}")
    else:
        print("Software version check is only applicable for websites.")

if __name__ == "__main__":
    main()
