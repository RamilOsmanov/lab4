from datetime import datetime , timedelta
currentday = datetime.now()
without = currentday.replace(microsecond=0)
print( currentday)
print( without)