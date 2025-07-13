
---

## Bash Script — `fim_check.sh`

```bash
#!/bin/bash

LOGFILE="/var/log/fim_check.log"
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

echo "[$TIMESTAMP] Running AIDE integrity check..." >> $LOGFILE
sudo aide --check >> $LOGFILE 2>&1

# Optional: Run Python parser if alerting is enabled
if [ -f "./fim_alert.py" ]; then
    python3 ./fim_alert.py $LOGFILE
fi
