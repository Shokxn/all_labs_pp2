import datetime

x = datetime.datetime.now()

y = x.strftime('%Y-%m-%d %H:%M:%S')

print("With microseconds: ", x)
print("Without microseconds: ", y)