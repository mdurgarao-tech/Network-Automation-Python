# Network Automation with Python

Python scripts that automate routine network and security operations tasks — IP/subnet validation, connectivity testing, configuration backups, and log parsing. Built to reduce manual effort and human error in day-to-day network security work.

This repo collects automation I've written and used as a Network Security Engineer to speed up repetitive operational tasks.

---

## Scripts

### 1. IP & Subnet Validation
Validates IP addresses and subnet inputs before they're used in configs or change requests — catches malformed addresses, checks subnet membership, and confirms whether a host belongs to a given network.
- **Use case:** pre-validating firewall rule inputs and avoiding bad entries during change windows.
- **Key libraries:** `ipaddress`

### 2. Ping / Connectivity Test Automation
Automates reachability checks across a list of hosts or devices and reports which are up or down — useful for quick health checks across many devices at once.
- **Use case:** post-change validation, troubleshooting connectivity outages, bulk reachability checks.
- **Key libraries:** `subprocess` / `ping3`, `csv`

### 3. Configuration Backup Automation
Automates pulling and saving device/configuration data on a schedule, so backups are consistent and timestamped instead of manual.
- **Use case:** keeping reliable config snapshots for audit, rollback, and change tracking.
- **Key libraries:** `paramiko` / `netmiko` (SSH), `os`, `datetime`

### 4. Log & Output Parsing
Parses log files and command output to extract the relevant lines — filtering noise, pulling out events of interest, and summarizing results.
- **Use case:** speeding up incident triage and finding root cause in large logs.
- **Key libraries:** `re`, file I/O

---

## Topics / Keywords
`Python` · `Network Automation` · `IP/Subnet Validation` · `Connectivity Testing` · `Config Backup` · `Log Parsing` · `Netmiko` · `Paramiko` · `Network Operations` · `Scripting`

---

## Repository structure
```
network-automation-python/
├── README.md
├── ip_subnet_validator.py
├── ping_test.py
├── config_backup.py
├── log_parser.py
└── sample_data/
    └── hosts.csv
```

---

## How to run
```bash
# Example
python3 ip_subnet_validator.py
python3 ping_test.py --input sample_data/hosts.csv
```
> Update device details, credentials, and file paths to match your environment. Do not commit real credentials — use environment variables or a local config file that's git-ignored.

---

## Notes
- Scripts are written for lab and operational use; sanitize any device names, IPs, or credentials before pushing to a public repo.
- Credentials should never be hard-coded — use `os.environ` or a `.env` file excluded via `.gitignore`.

---

**Author:** Miriyala Durga Rao — Network Security Engineer
[Portfolio](https://mdurgarao-tech.github.io) · [LinkedIn](https://www.linkedin.com/in/miriyala-durgarao)
