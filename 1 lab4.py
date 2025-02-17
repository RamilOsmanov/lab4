from datetime import datetime , timedelta
currentday = datetime.now()
now = currentday - timedelta(days=5)
print(currentday.strftime("%Y,%m,%d"))
print(now.strftime("%Y,%m,%d"))