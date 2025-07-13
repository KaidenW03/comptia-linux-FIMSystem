#!/usr/bin/env python3

import sys
import re

def alert_on_changes(log_file):
    suspicious = []
    with open(log_file, 'r') as f:
        for line in f:
            if re.search(r'^\s*Changed\s+file:', line) or re.search(r'^\s*Added\s+file:', line) or re.search(r'^\s*Removed\s+file:', line):
                suspicious.append(line.strip())

    if suspicious:
        print("\n🚨 Suspicious changes detected:")
        for entry in suspicious:
            print(f"  - {entry}")
    else:
        print("\n✅ No suspicious changes detected.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 fim_alert.py /path/to/logfile")
        sys.exit(1)
    alert_on_changes(sys.argv[1])
