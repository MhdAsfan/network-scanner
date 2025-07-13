import os
import platform

def ping(ip):
    # Determine the ping command based on the OS
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    # Run the ping command
    command = f"ping {param} 1 {ip}"
    return os.system(command) == 0

def scan_network(base_ip):
    live_hosts = []
    for i in range(1, 255):
        ip = f"{base_ip}.{i}"
        if ping(ip):
            live_hosts.append(ip)
    return live_hosts

if __name__ == "__main__":
    # Ask the user for the base IP address
    base_ip = input("Enter the base IP address (e.g., 192.168.1): ")

    # Scan the network
    live_hosts = scan_network(base_ip)

    # Print the results
    if live_hosts:
        print("Live hosts found:")
        for ip in live_hosts:
            print(f"Host {ip} is alive")
    else:
        print("No live hosts found.")
