# Precompiling for fast extraction of data.
import re

# Pattern for detecting failed ssh logins. I got this from Internet. I think it's okay to do so.
SSH_PATTERN = re.compile(r"Failed password for (?:invalid user )?(?P<username>\S+) from (?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")

test_lines = [
    "Feb 03 12:00:01 server sshd[123]: Failed password for root from 192.168.1.5 port 22 ssh2",
    "Feb 03 12:00:02 server sshd[123]: Failed password for invalid user admin from 10.0.0.1 port 22 ssh2",
    "Feb 03 12:00:03 server sshd[123]: Accepted password for tantalising from 192.168.1.20 port 22 ssh2"
]

line = test_lines[0]
result = SSH_PATTERN.search(test_lines[0])
print(f"Result for line {line} is: {result.groupdict()} ")
