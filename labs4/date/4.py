from datetime import datetime

def date_difference_in_seconds(date1: str, date2: str, date_format: str = "%Y-%m-%d %H:%M:%S")  -> int:
    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)

    return abs(int((d2 - d1).total_seconds()))

date1 = "2025-03-03 23:23:12"
date2 = "2025-03-04 12:35:23"

diff = date_difference_in_seconds(date1, date2)
print(f"Difference in seconds: {diff}")