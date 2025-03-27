import calendar


# print(calendar.calendar(2025))
# print(calendar.calendar(2025, 5)) # espaços
# print(calendar.month(2025, 5))
first_day, last_day = calendar.monthrange(2025, 3)
print(last_day)

print(calendar.day_name[calendar.weekday(2025, 3, last_day)])
