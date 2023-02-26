from datetime import datetime, timezone


def utc_datetime():
    return datetime.now(timezone.utc)
