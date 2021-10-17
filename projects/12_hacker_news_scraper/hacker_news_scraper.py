#!/usr/bin/env python
# coding: utf-8

# In[47]:


import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

target = 'bitcoin'
res_file = 'results.csv'
num_pages = 10
results = []


# In[48]:


for i in tqdm(range(1, num_pages+1)):
#     print(f'>>> Processing page {i}')
#     print('#', end='')
    resp = requests.get(f'https://news.ycombinator.com/news?p={i}')
    if resp.status_code != 200:
        break
    soup = BeautifulSoup(resp.content, 'html.parser')
    links = soup.find_all('a', class_='storylink')

    for link in links:
        if target in link.text.lower():
            _data = (link.text, link['href'])
            results.append(_data)


# In[42]:


print(f'Found {len(results)} links')


# In[43]:


import pandas as pd

my_data = pd.DataFrame(results, columns=['Text', 'Link'])

try:
    my_data.to_csv(res_file)
    print(f'Successfully saved to {res_file}')
except Exception as e:
    print('Failed to save results')
    print(e)
    


# In[44]:


my_data.head()

