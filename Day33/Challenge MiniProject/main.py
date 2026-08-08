import requests
import csv
import time
import logging

logging.basicConfig(
    filename="Day33/website_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
websites = [
    "https://example.com",
    "https://python.org",
    "https://github.com"
]

with open("Day33/Summary.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Website", "Status", "Response Time (seconds)"])
    print(f"{'Website':<30} {'Status':<10} {'Response Time':<15}")
    print("-" * 60)

    for website in websites:
        start = time.perf_counter()

        try:
            response = requests.get(website, timeout=5)
            status = response.status_code
            logging.info("%s --> %s",website,status)
        except requests.exceptions.RequestException as error:
            status = "DOWN"
            logging.error("%s -> DOWN | %s",website,error)

        end = time.perf_counter()
        total = end - start

        print(f"{website:<30} {str(status):<10} {total:.3f} sec")


        writer.writerow([website, status, f"{total:.3f}"])