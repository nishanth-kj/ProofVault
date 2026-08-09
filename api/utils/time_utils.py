import time


def current_milli_time() -> int:
    """
    Returns the current time in milliseconds since the Epoch.
    Suitable for BigInteger database columns.
    """
    return int(time.time() * 1000)
