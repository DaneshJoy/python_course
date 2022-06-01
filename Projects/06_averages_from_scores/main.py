import os, sys
from collections import Counter 
from text_reader import get_data_from_text_file
import pprint


os.system('cls')  # We used this line to have working colors in cmd
ppt = pprint.PrettyPrinter()
path = 'dataset'
list_of_files = os.listdir(path)

result_dict = {}
for filename in list_of_files:
    # Method 1 for join paths
    # filepath = path + '/' + filename
    # Method 2
    filepath = os.path.join(path, filename)
    try:
        with open(filepath, 'r') as f:
            my_data = f.readlines()
    except:
        print(f'Error reading from file: {filepath}')
        sys.exit()

    scores_dict = get_data_from_text_file(my_data)
    scores = scores_dict.values()
    average = sum(scores) / len(scores)

    # Extract student name from filename
    student_name = filename.split('.')[0]

    result_dict[student_name] = round(average, 2)

    print(f'\033[95m {student_name}: \033[92m{average:0.2f} \033[0m')
            
# Sort results dictionary (Descending)
result_sorted = Counter(result_dict).most_common()
# Ascending results using reverse method
# result_sorted.reverse()
# ppt.pprint(result_sorted)

# %% Write results to a file
out_file = 'results.txt'
try:
    with open(out_file, 'w') as f:
        for name, average in result_sorted:
            s = f'{name}: {average}\n'
            f.write(s)
except:
    print('Can not create results file')
        

