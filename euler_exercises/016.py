
x = 2 ** 1000
s = str(x)
s_list = list(s)

# Method 1
sum_all = 0
for i in s_list:
    sum_all += int(i)

# Method 2 (List Comprehension)
s_list_int = [int(j) for j in s_list]
sum_all_2 = sum(s_list_int)

print(sum_all)
print(sum_all_2)