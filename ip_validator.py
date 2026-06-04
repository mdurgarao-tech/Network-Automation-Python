import ipaddress

ip = input("Enter IP Address: ")

try:
    ipaddress.ip_address(ip)
    print("Valid IP Address")
except ValueError:
    print("Invalid IP Address")
