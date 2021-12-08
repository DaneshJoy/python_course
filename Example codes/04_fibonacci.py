''' Fibonacci Sequence 
Project Euler Problem 2'''

a = 0
b = 1
c = a+b

sum_even = 0
while c < 4000000:
    if c%2 == 0:
        sum_even += c
    c = a+b
    a = b
    b = c


print(sum_even)