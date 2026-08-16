import re
from collections import Counter


def read_log_file(file_name):
    with open(file_name, "r") as file:
        return file.readlines()


def find_ip_addresses(lines):
    pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    ips = []

    for line in lines:
        ips.extend(re.findall(pattern, line))

    return Counter(ips)



def count_failed_logins(lines):
    return sum("Failed password" in line for line in lines)


def find_suspicious_ips(ip_counts, limit=3):
    return {
        ip: count
        for ip, count in ip_counts.items()
        if count >= limit
    }