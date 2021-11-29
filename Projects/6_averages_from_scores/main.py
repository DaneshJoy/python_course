#!/usr/bin/env python
# ## Read Text Files in Python

import os
from text_reader import get_data_from_text_file

path = 'dataset'
list_of_files = os.listdir(path)

for filename in list_of_files:
    # Method 1 for join paths
    # filepath = path + '/' + filename
    # Method 2
    filepath = os.path.join(path, filename)
    with open(filepath, 'r') as f:
        my_data = f.readlines()
        scores_dict = get_data_from_text_file(my_data)

        scores = scores_dict.values()
        average = sum(scores) / len(scores)
        print(f'{average:0.2f}')

