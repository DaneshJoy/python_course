import pickle


mydict = {'a': [1,2,3,4],
          'b': 'salam',
          'c': {
              'f': (1,2,3),
              'g': True}
          }

with open('mydata.pkl', 'wb') as f:
    pickle.dump(mydict, f)


with open('mydata.pkl', 'rb') as f2:
    mydict2 = pickle.load(f2)