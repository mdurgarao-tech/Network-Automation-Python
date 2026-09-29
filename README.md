# Network Automation with Python

Small Python scripts for routine network checks. Standard library only, no installs needed.

## Scripts

### ip_validator.py
Checks whether IP addresses are valid (IPv4 or IPv6) and, optionally, whether they fall inside a network.

```bash
python3 ip_validator.py 10.0.0.5 192.168.1.300 2001:db8::1
python3 ip_validator.py 10.0.0.5 10.0.1.9 --network 10.0.0.0/24
```

Exits with code 1 if any address is invalid.

### ping_test.py
Pings one or more hosts and reports each as UP or DOWN. Hosts can be given on the command line or read from a text file (one per line, `#` for comments).

```bash
python3 ping_test.py 8.8.8.8 example.com
python3 ping_test.py --file hosts.txt --count 3
```

Every target is checked as a valid IP or hostname before it is passed to ping, and ping runs without a shell, so input like `8.8.8.8; ls` is rejected instead of executed. Exits with code 1 if any host is down or invalid.

## Testing

The input validation and error handling have been tested locally. The UP/DOWN result depends on ping and network access on your machine.

## Planned next

- Simple log parsing for firewall and WAF exports

Not built yet.

---

**Author:** Miriyala Durga Rao
[LinkedIn](https://www.linkedin.com/in/miriyala-durgarao) · [Portfolio](https://edgeguard-chronicle.lovable.app)
