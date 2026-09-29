"""Ping one or more hosts and report which are up or down.

Examples:
    python3 ping_test.py 8.8.8.8 example.com
    python3 ping_test.py --file hosts.txt

hosts.txt holds one IP or hostname per line. Blank lines and lines
starting with # are ignored.
"""
import argparse
import ipaddress
import platform
import re
import subprocess
import sys

# Letters, digits and hyphens per label; a label cannot start or end with a hyphen.
HOSTNAME_RE = re.compile(
    r"^(?=.{1,253}$)[A-Za-z0-9]([A-Za-z0-9-]{0,61}[A-Za-z0-9])?"
    r"(\.[A-Za-z0-9]([A-Za-z0-9-]{0,61}[A-Za-z0-9])?)*$"
)


def is_valid_target(host):
    """Accept only a valid IP address or hostname, so nothing odd reaches ping."""
    try:
        ipaddress.ip_address(host)
        return True
    except ValueError:
        return bool(HOSTNAME_RE.match(host))


def ping(host, count=2, timeout=2):
    """Return True if the host answers. Runs ping without a shell."""
    count_flag = "-n" if platform.system().lower() == "windows" else "-c"
    cmd = ["ping", count_flag, str(count), host]
    try:
        result = subprocess.run(
            cmd, capture_output=True, timeout=count * timeout + 5
        )
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False
    return result.returncode == 0


def read_hosts(path):
    with open(path) as f:
        lines = (line.strip() for line in f)
        return [line for line in lines if line and not line.startswith("#")]


def main():
    parser = argparse.ArgumentParser(description="Ping hosts and report status.")
    parser.add_argument("hosts", nargs="*", help="IPs or hostnames to ping")
    parser.add_argument("--file", help="text file with one host per line")
    parser.add_argument("--count", type=int, default=2, help="pings per host")
    args = parser.parse_args()

    hosts = list(args.hosts)
    if args.file:
        hosts += read_hosts(args.file)
    if not hosts:
        parser.error("give at least one host, or use --file")

    down = 0
    for host in hosts:
        if not is_valid_target(host):
            print(f"{host}: SKIPPED (not a valid IP or hostname)")
            down += 1
        elif ping(host, count=args.count):
            print(f"{host}: UP")
        else:
            print(f"{host}: DOWN")
            down += 1

    sys.exit(1 if down else 0)


if __name__ == "__main__":
    main()
