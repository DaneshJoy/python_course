import requests
from bs4 import BeautifulSoup
import pickle
import json
# from urllib.parse import unquote
from requests.utils import unquote

# Boilerplate
links = ['https://www.2nabsh.com/%D8%A7%D9%85%D9%84%D8%A7%DA%A9-%D8%AA%D9%87%D8%B1%D8%A7%D9%86/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4-%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D9%82%DB%8C%D9%85%D8%AA-%D8%AA%D8%A7-3-%D9%85%DB%8C%D9%84%DB%8C%D8%A7%D8%B1%D8%AF',
          'https://www.2nabsh.com/%D8%A7%D9%85%D9%84%D8%A7%DA%A9-%D8%AA%D9%87%D8%B1%D8%A7%D9%86/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4-%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86?min_price=3000000000&max_price=5000000000',
          'https://www.2nabsh.com/%D8%A7%D9%85%D9%84%D8%A7%DA%A9-%D8%AA%D9%87%D8%B1%D8%A7%D9%86/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4-%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86?min_price=5000000000&max_price=7000000000',
          'https://www.2nabsh.com/%D8%A7%D9%85%D9%84%D8%A7%DA%A9-%D8%AA%D9%87%D8%B1%D8%A7%D9%86/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4-%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86?min_price=7000000000&max_price=10000000000',
          'https://www.2nabsh.com/%D8%A7%D9%85%D9%84%D8%A7%DA%A9-%D8%AA%D9%87%D8%B1%D8%A7%D9%86/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4-%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%AA%D9%87%D8%B1%D8%A7%D9%86%D9%BE%D8%A7%D8%B1%D8%B3',
          'https://www.2nabsh.com/%D8%A7%D9%85%D9%84%D8%A7%DA%A9-%D8%AA%D9%87%D8%B1%D8%A7%D9%86/%D8%AE%D8%B1%DB%8C%D8%AF-%D9%81%D8%B1%D9%88%D8%B4-%D8%A2%D9%BE%D8%A7%D8%B1%D8%AA%D9%85%D8%A7%D9%86/%D8%B3%D8%B9%D8%A7%D8%AF%D8%AA-%D8%A2%D8%A8%D8%A7%D8%AF'
          ]


results_dict = {}

for i, lnk in enumerate(links):
    print(f'Processing page {i+1}...')
    resp = requests.get(lnk)
    content = resp.text
    
    soup = BeautifulSoup(content, 'html.parser')
    
    cards = soup.find_all('div', class_='sc-161sqt8-1 fiWed d-flex flex-column')
    
    for j, card in enumerate(cards):
        desc = card.find('address', class_='sc-18pxd7r-3 jRKKyg text-ellipsis')
        desc = desc.text.strip()
        desc = desc.split('،')[0].strip()
        
        price = card.find('span', class_='s50ua-0 cjJLH font-weight-normal')
        price = price.text.strip()
        
        # print(f'{i*20+(j+1)} {desc} قیمت {price}')
        key = i*20+(j+1)
        results_dict[key] = [desc, price]
        
# %% Save results

with open('data.pkl', 'wb') as f:
    pickle.dump(results_dict, f)
    
with open('data.json', 'w', encoding='utf8') as f:
    json.dump(results_dict, f, indent=4, ensure_ascii=False)    
        
        
        
        
    