# File Integrity Monitoring (FIM) System

This project implements a basic File Integrity Monitoring (FIM) system using AIDE (Advanced Intrusion Detection Environment) along with custom Bash and Python scripts. The system monitors changes in critical system directories such as `/etc`, `/bin`, and `/usr` to detect potential unauthorized modifications, which may indicate a security breach.

## 🛠️ Tools Used
- **AIDE**: Core integrity checker.
- **Bash**: For initialization and scheduled checks.
- **Python**: For parsing and alerting on suspicious changes (optional extension).
- **cron**: For scheduling automated checks.

## 📂 Directories Monitored
- `/etc`
- `/bin`
- `/usr`
- Add more as needed in the AIDE configuration.

## 🚀 Setup

### 1. Install AIDE

sudo apt update && sudo apt install aide -y

### 2. Running AIDE
sudo aideinit
sudo cp /var/lib/aide/aide.db.new /var/lib/aide/aide.db

### 3. Schedule Regular Checks
Use the provided Bash script to automate integrity checks. Schedule is using cron for regular intervals

### 4. Parse and Alert
Use the python script to parse the AIDE output and alert or log suspicious changes
