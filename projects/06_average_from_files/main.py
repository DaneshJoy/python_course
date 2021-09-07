'''
Calculate Moaddel from Files
'''

import os
import utils
from collections import Counter

# Get list of files in a directory
grade_files = os.listdir('dataset')

result = []
result_dict = {}
for file in grade_files:
    _file = 'dataset/' + file
    # Get grades and lessons in a dictionary
    grades_dict = utils.get_data_from_file(_file)
    # Get only grades
    nomreha = list(grades_dict.values())
    # Calculate average
    _moaddel = sum(nomreha) / len(nomreha)
    _moaddel = round(_moaddel, 2)
    
    # Get student name from filename
    _std_name = file.split('.')[0]
    
    result.append(f'{_std_name} : {_moaddel}\n')
    result_dict[_std_name] = _moaddel
    print(f'{_std_name} : {_moaddel}')
    

result_dict_sorted = Counter(result_dict).most_common()

result_final = []
for item in result_dict_sorted:
    _tmp = f'{item[0]} : {item[1]}\n'
    result_final.append(_tmp)
    
with open('moaddels.txt', 'w') as f:
    f.writelines(result_final)
    
    
    

