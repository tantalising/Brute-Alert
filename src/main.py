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

for line in follow_file(LOG_PATH):
    print(line)