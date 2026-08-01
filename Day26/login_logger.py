"""Record login attempts and keep failed attempts in a separate log."""

import logging
import platform
from pathlib import Path


LOG_DIRECTORY = Path(__file__).resolve().parent
ALL_EVENTS_LOG = LOG_DIRECTORY / "security_events.log"
FAILED_EVENTS_LOG = LOG_DIRECTORY / "failed_events.log"
LOG_FORMAT = "%(asctime)s | %(levelname)s | %(message)s"


def create_logger(name: str, log_file: Path) -> logging.Logger:
    """Return a logger that writes to one file without duplicate handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if not logger.handlers:
        handler = logging.FileHandler(log_file, encoding="utf-8")
        handler.setFormatter(logging.Formatter(LOG_FORMAT))
        logger.addHandler(handler)

    return logger


all_events_logger = create_logger("login_events", ALL_EVENTS_LOG)
failed_events_logger = create_logger("failed_login_events", FAILED_EVENTS_LOG)


def total_failed_logins() -> int:
    """Count failed attempts previously saved in failed_events.log."""
    if not FAILED_EVENTS_LOG.exists():
        return 0

    with FAILED_EVENTS_LOG.open(encoding="utf-8") as log_file:
        return sum(1 for line in log_file if "Status=Failed" in line)


def record_login(username: str, status: str, ip_address: str) -> None:
    status = status.strip().title()
    device_name = platform.node() or "Unknown device"
    event = (
        f"User={username} Status={status} IP={ip_address} "
        f"DeviceName={device_name}"
    )

    # The timestamp written by the logging formatter is the login time.
    all_events_logger.info(event)

    if status == "Failed":
        failed_events_logger.warning(event)


if __name__ == "__main__":
    username = input("Username: ").strip()
    status = input("Login Status (Success/Failed): ").strip()
    ip_address = input("IP Address: ").strip()

    record_login(username, status, ip_address)
    print("Login event saved successfully.")
    print(f"Total failed logins: {total_failed_logins()}")
