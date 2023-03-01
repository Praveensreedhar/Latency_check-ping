import subprocess
from influxdb import InfluxDBClient
import influxdb
import subprocess, sys
import os
import re

os.chdir("/AUTOMATION/GW-LATENCY-CHECK/")
gateways = open('gateway.txt')

for gateway in gateways:
    host = gateway.strip()
    #host = "10.10.1.1"
    ping_count = 2  # Number of pings to send
    ping_command = ["ping", "-c", str(ping_count), host]
    ping_output = subprocess.Popen(ping_command, stdout=subprocess.PIPE).stdout.read().decode()


    # Extract the average round-trip time from the output
    rtt_pattern = r"min/avg/max/mdev = \d+\.\d+/(\d+\.\d+)/\d+\.\d+/\d+\.\d+"
    rtt_match = re.search(rtt_pattern, ping_output)

    if rtt_match:
        rtt = float(rtt_match.group(1))
        print(f"Average RTT to {host}: {rtt} ms")
    else:
        print(f"Failed to get RTT for {host}")
