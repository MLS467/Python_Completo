from datetime import datetime

fmt = "%d/%m/%Y"
data = datetime(2025, 3, 26, 7, 59, 23)

print(data.strftime(fmt))
print(data.strftime("%Y"), data.year)
print(data.strftime("%m"), data.month)
