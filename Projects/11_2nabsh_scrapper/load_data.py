import pickle
import json


with open('data.pkl', 'rb') as f:
    data1 = pickle.load(f)
    
with open('data.json', 'r') as f:
    data2 = json.load(f)


print(data1)
print(data2)