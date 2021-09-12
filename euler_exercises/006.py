# Method 1
sum_of_squares = 0
sum_all = 0

for i in range(1, 101):
    sum_of_squares += i**2
    sum_all += i

square_of_sum = sum_all ** 2

print(square_of_sum - sum_of_squares)

# Method 2

n = 100
sum_of_squares = (n*(n+1)*(2*n+1))/6
square_of_sum = (n*(n+1)/2) ** 2
print(int(square_of_sum - sum_of_squares))
    