
sum_all = 0
n = 1000
for i in range(3,n):
    if (i%3 == 0) or (i%5 == 0):
        sum_all += i

print(sum_all)