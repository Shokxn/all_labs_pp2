import datetime

x = datetime.datetime.now()
y = datetime.timedelta(days = 5)

date = x - y

print("Current time: ", x.strftime('%Y-%m-%d'))
print("5 days agoxs: ", date.strftime('%Y-%m-%d'))