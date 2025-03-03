import datetime

today = datetime.datetime.now()
interval = datetime.timedelta(days=1)
tomorrow = today + interval
yesterday = today - interval

print("Yesterday: ", yesterday.strftime('%Y-%m-%d'))
print("Today: ", today.strftime('%Y-%m-%d'))
print("Tomorrow: ", tomorrow.strftime('%y-%m-%d'))