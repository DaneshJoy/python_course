# Calculate average of scores

scores = input('enter your scores:')
scores_list = scores.split()

# Method 1
# scores_list2 = [float(i) for i in scores_list]
# my_sum = sum(scores_list2)

# Method 2
my_sum = 0
for s in scores_list:
    my_sum = my_sum + float(s)

avg = my_sum / len(scores_list)

print(avg)
