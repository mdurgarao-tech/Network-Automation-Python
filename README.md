# Network Automation with Python

Small Python scripts for routine network checks. This is a starter repo. It currently has two basic scripts, and I'm adding more as I build them.

## What's in the repo

| File | What it does |
|---|---|
| `ip_validator.py` | Asks for an IP address and checks whether it is valid (IPv4 or IPv6) using Python's `ipaddress` module. |
| `ping_test.py` | Asks for a host and pings it. |

## How to run

```bash
python3 ip_validator.py
python3 ping_test.py
```

Both scripts use only the Python standard library.

## Planned next

- Bulk reachability checks from a CSV of hosts
- Subnet membership checks (is this host inside this network?)
- Simple log parsing for firewall and WAF exports

These are not built yet.

---

**Author:** Miriyala Durga Rao
[LinkedIn](https://www.linkedin.com/in/miriyala-durgarao) · [Portfolio](https://edgeguard-chronicle.lovable.app)
