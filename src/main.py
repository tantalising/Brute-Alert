import os
import time
from typing import Generator
from parser import get_login_info

LOG_PATH = "test.log" #"/var/log/auth.log"
HIGHEST_TRY = 5

def follow_file(filepath):
    if not os.path.exists(filepath):
        print(f"Error: Log file not found at {filepath}")
        return

    with open(filepath, 'r') as f:
        f.seek(0, os.SEEK_END)
        
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5) # let the cpu take some rest.
                continue
            yield line

failed_attempts = {}

for line in follow_file(LOG_PATH):
    match = get_login_info(line)
    if match:
        ip = match['ip']
        if ip in failed_attempts:
            failed_attempts[ip] += 1
            print(f"status is {failed_attempts}")
        else:
            failed_attempts[ip] = 1

print(f"status is {failed_attempts}")