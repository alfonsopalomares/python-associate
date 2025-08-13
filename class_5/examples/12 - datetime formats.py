from datetime import date, time, datetime

dt = datetime(2019, 11, 4, 14, 53)
d = date(2020, 1, 4)
t = time(14, 53)

print(d.strftime("%Y/%m/%d"))
print(t.strftime("%H:%M:%S"))
print(dt.strftime("%y/%B/%d %H:%M:%S"))
