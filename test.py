
# # Method 1
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     for line in data:
#         print(line)

# # Method 2
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         print(row)
        
# Method 2
import pandas
data = pandas.read_csv("weather_data.csv")
temp_list = data["temp"].to_list() # list(data["temp"])
data_dict = data.to_dict()

temp_mean = sum(temp_list) / len(temp_list)
temp_mean2 = data["temp"].mean()
temp_max = data["temp"].max()