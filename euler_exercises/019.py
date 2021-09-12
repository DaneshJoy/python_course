from datetime import datetime

sundays = 0
for y in range(1901, 2001):
    for m in range(1,13):
        x = datetime(y, m, 1)
        if x.weekday() == 6:
            sundays += 1
            
print(sundays)