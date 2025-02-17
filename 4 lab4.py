from datetime import datetime

date1 = datetime(2006, 8, 2, 12, 30, 0)
date2 = datetime(2025, 2, 16, 8, 15, 0)

difference = date1 - date2
diffeinsec = difference.total_seconds()

print(int(diffeinsec))
