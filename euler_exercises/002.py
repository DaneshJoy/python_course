from timeit import default_timer

# Method 1


start = default_timer()

a = 1
b = 2
c = a+b
sum_all = 2
while c < 4000000:
    c = a+b
    a = b
    b = c
    
    if c%2 == 0:
        sum_all += c

end = default_timer()

elapsed_time = end - start
print(sum_all)
print(f'time: {elapsed_time:.2} seconds')


# Method 2 (Recursive Function)
def fib(n):
    if n==1 or n==2:
        return n
    else:
        result = fib(n-1) + fib(n-2)
        return result

start = default_timer()
sum_all = 0
i = 0
c = 0
while c < 4000000:
    i += 1
    c = fib(i)
    if c%2 == 0:
        sum_all += c

end = default_timer()
elapsed_time = end - start
print(sum_all)
print(f'time: {elapsed_time:.2} seconds')

    