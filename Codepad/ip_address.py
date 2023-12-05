import re

def find_repeated_ip_addresses(log_file_path):
    # Read the log file
    with open(log_file_path, 'r') as file:
        log_data = file.read()

    # Define a regular expression pattern to match IP addresses
    ip_pattern = re.compile(r"((\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}))")

    # Find all matches of IP addresses in the log data
    ip_addresses = ip_pattern.findall(log_data)
    print(ip_addresses)

    # Count the occurrences of each IP address using a dictionary
    ip_count = {}
    for ip in ip_addresses:
        if ip in ip_count:
            ip_count[ip] += 1
        else:
            ip_count[ip] = 1
    # Filter out IP addresses that occurred more than once
    repeated_ips = {ip: count for ip, count in ip_count.items() if count > 1}

    return repeated_ips

# Example usage
log_file_path = "test.txt"
repeated_ips = find_repeated_ip_addresses(log_file_path)

# Print the repeated IP addresses and their counts
for ip, count in repeated_ips.items():
    print(f"IP Address: {ip}, Count: {count}")