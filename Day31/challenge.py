import csv
import hashlib
from multiprocessing import Pool, cpu_count
from time import perf_counter


def calculate_hashes(filename):
    try:
        with open(filename, "rb") as file:
            data = file.read()

        return {
            "filename": filename,
            "md5": hashlib.md5(data).hexdigest(),
            "sha256": hashlib.sha256(data).hexdigest(),
            "status": "Success"
        }

    except FileNotFoundError:
        return {
            "filename": filename,
            "md5": "",
            "sha256": "",
            "status": "File not found"
        }


def save_to_csv(results, output_file):
    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["filename", "md5", "sha256", "status"]
        )
        writer.writeheader()
        writer.writerows(results)


if __name__ == "__main__":
    files = [
        "Day31/file1.txt",
        "Day31/file2.txt",
        "Day31/file3.txt",
        "Day31/file4.txt"
    ]

    # Sequential execution
    start = perf_counter()

    sequential_results = []
    for filename in files:
        sequential_results.append(calculate_hashes(filename))

    sequential_time = perf_counter() - start

    # Parallel execution
    start = perf_counter()

    with Pool(processes=cpu_count()) as pool:
        parallel_results = pool.map(calculate_hashes, files)

    parallel_time = perf_counter() - start

    # Save parallel results to CSV
    save_to_csv(parallel_results, "Day31/file_hashes.csv")

    print("Sequential time:", round(sequential_time, 4), "seconds")
    print("Parallel time:", round(parallel_time, 4), "seconds")
    print("Results saved to file_hashes.csv")
    
    
    
    """
    🛡️ Cybersecurity Practice
Password Hash Generator (Educational)
import hashlib

passwords = [
    "admin123",
    "cyber123",
    "password1"
]

for password in passwords:
    print(
        hashlib.sha256(
            password.encode()
        ).hexdigest()
    )
Challenge

Use a process pool to hash a larger list of passwords in parallel and compare the runtime to a sequential version.
"""