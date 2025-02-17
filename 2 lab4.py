from datetime import datetime , timedelta
currentday = datetime.now()
yest = currentday - timedelta(days=1)

tomw = currentday + timedelta(days=1)
print(yest.strftime("%Y,%m,%d"))
print(currentday.strftime("%Y,%m,%d"))
print(tomw.strftime("%Y,%m,%d"))
