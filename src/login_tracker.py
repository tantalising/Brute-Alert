import asyncio
from datetime import datetime

class LoginTracker:
    def __init__(self, waiting_period, highest_try):
        self._failed_attempts = {}
        self.task = asyncio.create_task(self._start_clock(waiting_period))
        self._highest_try = highest_try

    async def _start_clock(self, seconds):
        while True:
            await asyncio.sleep(seconds)
            self._failed_attempts.clear()
    
    def _print_if_too_many_attempt(self, ip):
        current_try = self._failed_attempts[ip]
        if current_try >= self._highest_try:
            print(f'ALERT! Brute force attempt detected from ip: {ip} at {self._current_time()}')
    
    def _current_time(self):
        now = datetime.now()
        time = now.strftime("%I:%M %p %d-%m-%Y")
        return time
    
    def increase_login_count(self, ip):
        self._failed_attempts[ip] += 1
        self._print_if_too_many_attempt(ip)
    
    def log(self, ip):
        if self.exists(ip):
            return
        self._failed_attempts[ip] = 1   

    def exists(self, ip):
        return ip in self._failed_attempts 
