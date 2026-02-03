import asyncio

class LoginTracker:
    def __init__(self, waiting_period, highest_try):
        self._failed_attempts = {}
        self.task = asyncio.create_task(self._start_clock(waiting_period))
        self._highest_try = highest_try

    async def _start_clock(self, seconds):
        while True:
            print('clock started')
            await asyncio.sleep(seconds)
            print("clearing attempts")
            self._failed_attempts.clear()
    
    def _print_if_too_many_attempt(self, ip):
        current_try = self._failed_attempts[ip]
        if current_try >= self._highest_try:
            print(f'ALERT! Brute force attempt detected from ip: {ip}')
    
    def increase_login_count(self, ip):
        self._failed_attempts[ip] += 1
        self._print_if_too_many_attempt(ip)
    
    def log(self, ip):
        if self.exists(ip):
            return
        self._failed_attempts[ip] = 1   

    def exists(self, ip):
        return ip in self._failed_attempts 
