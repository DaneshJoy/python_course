import json


mydict = {'a': [1,2,3,4],
          'b': 'salam',
          'c': {
              'f': (1,2,3),
              'g': True}
          }

with open('mydata.json', 'w') as f:
    json.dump(mydict, f)


with open('mydata.json', 'r') as f2:
    mydict2 = json.load(f2)