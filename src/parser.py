# Precompiling for fast extraction of data.
import re

# Pattern for detecting failed ssh logins. I got this from Internet. I think it's okay to do so.
SSH_PATTERN = re.compile(r"Failed password for (?:invalid user )?(?P<username>\S+) from (?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")

def get_login_info(log_line):
    match = SSH_PATTERN.search(log_line)
    if match:
        return match.groupdict()
    return None
