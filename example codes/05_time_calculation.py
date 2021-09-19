from timeit import default_timer
from time import sleep, process_time

start = default_timer()
start2 = process_time()

for i  in range(10000000):
    i += 1
sleep(2)

end = default_timer()
end2 = process_time()

elapsed = end-start
elapsed2 = end2-start2

# Including sleep time
print('time:', elapsed)

# not including sleep time
print('time:', elapsed2)