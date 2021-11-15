nomreha = [19.5, 14, 13, 20, 15, 14.75, 6]

# %% Method 1
s = 0
n = 0
for i in nomreha:
    # calculate sum
    s = s + i
    # Calculate number of items
    n = n+1

average1 = s / n
print("Average with method 1 is:", average1)

# %% Method 2
average2 = sum(nomreha) / len(nomreha)
print("Average with method 2 is:", average2)
