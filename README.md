# Brute Alert

A lightweight, security utility designed to monitor Linux authentication logs in real-time. It detects potential brute-force attacks by tracking failed login attempts and triggering alerts when a specific threshold is exceeded within a defined time window.

# How to run
No external dependencies has been used.
Just clone the repo and run the main.py inside src folder.

# Configurations
Open main.py to adjust the configuration constants:

- LOG_PATH: Path to the log file (Default: test.log. Change to /var/log/auth.log for real use).
- HIGHEST_TRY: Max failed attempts allowed (Default: 5).
- WAITING_PERIOD: Time window in seconds (Default: 5).

# Design Decisions
 - Used asyncio as a modern lightweight way of handling asynchronous tasks.
 - Precompiled the log parsing regex for better speed even when there's a lot of logs being made in a short amount of time
 - Used a non blocking timer to periodically clear old logs so that no false positive alert is issued.

# Testing
When testing add a fake failed login line inside src/test.log file repeatedly like this:
`echo "Failed password for root from 10.11.12.13" >> test.log`
