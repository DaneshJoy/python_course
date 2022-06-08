
import os
import pandas as pd
from utils import calculate_bmi


os.system('cls')
# %% Part 1 - Load Data

# Read Data
data = pd.read_csv("hw_200.csv")

# Get Columns
# Method 1
heights = data["Height(Inches)"]
weights = data["Weight(Pounds)"]

# # Method 2
# heights = data.iloc[:, 1]
# weights = data.iloc[:, 2]

# %% Part 2 - Process Data

# Convert from Imperial to Metric
heights_metric = heights*2.54
weights_metric = weights/2.205

# Calculate BMI
# # Method 1
# for i in range(len(heights_metric)):
#     print(heights_metric[i])
#     print(weights_metric[i])

# Method 2  
calculated_bmis = []
for hh, ww in zip(heights_metric, weights_metric):
    calculated_bmis.append(calculate_bmi(hh, ww))

# %% Save Results

# 1- Convert lists to doctionary
result_dict = {"Index": data["Index"],
               "Height": heights_metric,
               "Weight": weights_metric,
               "BMI": calculated_bmis}

# 2- Convert dictionary to Pandas DataFrame
df = pd.DataFrame(result_dict)
df.set_index("Index", inplace=True)

# Report for Pandas Series
bmis = df['BMI']
print(f'\033[32m BMI max: \033[36m {bmis.max()} \033[0m')
print(f'\033[32m BMI min: \033[36m {bmis.min()} \033[0m')
print(f'\033[32m BMI average: \033[36m {bmis.mean():0.2f} \033[0m')

# 3- Save to file
if not os.path.exists('results'):
    os.mkdir('results')
    
df.to_csv("results/bmi_table.csv")
df.to_json("results/bmi_table.json")
df.to_html("results/bmi_table.html")
df.to_excel("results/bmi_table.xlsx")


