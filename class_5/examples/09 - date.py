from datetime import date

today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)


my_date = date(2019, 11, 4)
print(my_date)


# datetime from ISO format: YYYY-MM-DD

d = date.fromisoformat('2023-08-31')
print(d)

# week day.
print ("today weekday", today.weekday())
print ("my_date weekday", my_date.weekday())
print ("d weekday", d.weekday())
