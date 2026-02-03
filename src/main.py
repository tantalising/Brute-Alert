import os
import sys
import time
import asyncio
from login_tracker import LoginTracker
from parser import get_login_info

LOG_PATH = "test.log" #"/var/log/auth.log" <-- use this when not testing
HIGHEST_TRY = 5
WAITING_PERIOD = 5

async def follow_file(filepath):
    if not os.path.exists(filepath):
        print(f"Error: Log file not found at {filepath}")
        return

    with open(filepath, 'r') as f:
        f.seek(0, os.SEEK_END)
        
        while True:
            line = f.readline()
            if not line:
               await asyncio.sleep(0.5) # let the cpu take some rest.
               continue
            yield line


async def main():
    login_tracker = LoginTracker(WAITING_PERIOD, HIGHEST_TRY)
    async for line in follow_file(LOG_PATH):
        match = get_login_info(line)
        if match:
            ip = match['ip']
            if login_tracker.exists(ip):
                login_tracker.increase_login_count(ip)
            else:
                login_tracker.log(ip)

if __name__ == "__main__":
    print("Brute Force Detector Started. \nPress CTRL+C to exit.")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('\rExiting...')
        sys.exit(0)