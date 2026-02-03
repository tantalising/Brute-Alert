import os
import time
import asyncio
from typing import Generator
from parser import get_login_info

LOG_PATH = "test.log" #"/var/log/auth.log"
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

def print_if_too_many_attempt(current_try, highest_try, ip):
    if current_try >= highest_try:
        print(f'ALERT! Brute force attempt detected from ip: {ip}')


async def start_clock(seconds, attempts):
    while True:
        print('clock started')
        await asyncio.sleep(seconds)
        print("clearing attempts")
        attempts.clear()


failed_attempts = {}

async def main():
    asyncio.create_task(start_clock(WAITING_PERIOD, failed_attempts))
    async for line in follow_file(LOG_PATH):
        match = get_login_info(line)
        if match:
            ip = match['ip']
            if ip in failed_attempts:
                failed_attempts[ip] += 1
                print_if_too_many_attempt(failed_attempts[ip], HIGHEST_TRY, ip)
            else:
                failed_attempts[ip] = 1

    print(f"status is {failed_attempts}")

if __name__ == "__main__":
    asyncio.run(main())