import numpy as np
import glob
import os
from collections import Counter

files = glob.glob('dataset/*.txt')

# %% Read and process
averages = []
averages_dict = {}
for path in files:
    grades = []
    with open(path, 'r') as f:
        for line in f:
            l = line.strip()
            s = l.split(',')
            grades.append(float(s[1]))
    
    # Method 1
    # sum_ = 0
    # for i in range(len(grades)):
    #     sum_ = sum_ + grades[i]
    
    # avg = sum_ / len(grades)
    
    ## Method 2
    avg = sum(grades) / len(grades)
    
    filename = os.path.basename(path)
    filename = filename.split('.')[0]
    averages_dict[filename] = avg
    
    ## Method 3
    # avg = np.mean(grades)
    
    # print(avg)
    averages.append(avg)

averages.sort(reverse=True)
averages_sorted = Counter(averages_dict).most_common()
print(averages)

print("The best student's average is:", averages[0])

# %% Write results
with open('averages.txt','w') as f:
    for item in averages_sorted:
        f.write(str(item) + '\n')









