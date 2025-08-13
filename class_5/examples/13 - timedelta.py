from datetime import timedelta
from datetime import date
from datetime import datetime

delta = timedelta(weeks=2, days=2, hours=2)
print(delta)

delta2 = delta * 2
print(delta2)

d = date(2023, 10, 31) + delta2
print(d)

dt = datetime(2023, 6, 27, 14, 53) + delta2
print(dt)
