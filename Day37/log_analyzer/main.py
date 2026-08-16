from analyzer import (
    read_log_file,
    find_ip_addresses,
    count_failed_logins,
    find_suspicious_ips,
)


def main():
    lines = read_log_file("security.log")

    ip_counts = find_ip_addresses(lines)
    
    failed_logins = count_failed_logins(lines)
    suspicious_ips = find_suspicious_ips(ip_counts)

    print("Log Analysis Report")
    print("-" * 25)
   
    print(f"Failed login attempts: {failed_logins}")

    print("\nIP address activity:")
    for ip, count in ip_counts.items():
        print(f"{ip}: {count} occurrence(s)")

    print("\nSuspicious IP addresses (3+ occurrences):")
    if suspicious_ips:
        for ip, count in suspicious_ips.items():
            print(f"{ip}: {count} occurrence(s)")
            print("🚨 ALERT: Possible brute-force activity")
    else:
        print("None found.")


if __name__ == "__main__":
    main()