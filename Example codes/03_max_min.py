s = [14, 6, 50, 3, 55, 2, 33, 56, 23, 8, 59, 34, 67, 14]

# %% Method 1
max_ = min_ = s[0]
for i in s:
    if i > max_:
        max_ = i
    if i < min_:
        min_ = i

print('Maximum1 is:', max_)
print('Minimum1 is:', min_)

# %% Method 2
print('Maximum2 is:', max(s))
print('Minimum2 is:', min(s))
