# Precompiling for fast extraction of data.
import re

# Pattern for detecting failed ssh logins. I got this from Internet. I think it's okay to do so.
SSH_PATTERN = re.compile(r"Failed password for (?:invalid user )?(?P<username>\S+) from (?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")

def get_login_info(log_line):
    match = SSH_PATTERN.search(log_line)
    if match:
        return match.groupdict()
    return None

test_lines = [
    "Feb 03 12:00:01 server sshd[123]: Failed password for root from 192.168.1.5 port 22 ssh2",
    "Feb 03 12:00:02 server sshd[123]: Failed password for invalid user admin from 10.0.0.1 port 22 ssh2",
    "Feb 03 12:00:03 server sshd[123]: Accepted password for tantalising from 192.168.1.20 port 22 ssh2"
]

print("Testing Parser...")
for line in test_lines:
    result = get_login_info(line)
    print(f"Line: {line[:30]}... -> Result: {result}")
