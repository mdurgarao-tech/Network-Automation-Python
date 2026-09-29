"""Validate IP addresses and optionally check whether they belong to a network.

Examples:
    python3 ip_validator.py 10.0.0.5 192.168.1.300 2001:db8::1
    python3 ip_validator.py 10.0.0.5 10.0.1.9 --network 10.0.0.0/24
"""
import argparse
import ipaddress
import sys


def parse_ip(value):
    """Return an ip_address object, or None if the value is not a valid IP."""
    try:
        return ipaddress.ip_address(value.strip())
    except ValueError:
        return None


def main():
    parser = argparse.ArgumentParser(description="Validate IP addresses.")
    parser.add_argument("ips", nargs="+", help="one or more IP addresses to check")
    parser.add_argument(
        "--network",
        help="CIDR range to check membership against, e.g. 10.0.0.0/24",
    )
    args = parser.parse_args()

    network = None
    if args.network:
        try:
            network = ipaddress.ip_network(args.network, strict=False)
        except ValueError:
            sys.exit(f"Invalid network: {args.network}")

    invalid = 0
    for value in args.ips:
        ip = parse_ip(value)
        if ip is None:
            print(f"{value}: INVALID")
            invalid += 1
            continue

        line = f"{value}: valid IPv{ip.version}"
        if network is not None:
            if ip.version != network.version:
                line += f", not in {network} (different IP version)"
            elif ip in network:
                line += f", in {network}"
            else:
                line += f", not in {network}"
        print(line)

    sys.exit(1 if invalid else 0)


if __name__ == "__main__":
    main()
