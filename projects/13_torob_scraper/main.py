
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm


laptops = []
res_file = 'results.xlsx'

for i in tqdm(range(1, 6)):
    resp = requests.get(f'https://torob.com/browse/99/%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-%D9%88-%D9%86%D9%88%D8%AA-%D8%A8%D9%88%DA%A9-laptop/?page={i}')
    if resp.status_code != 200:
        print(f'Failed with status code: {resp.status_code}')
        break
    soup = BeautifulSoup(resp.content, 'html.parser')

    cards = soup.find_all('div', class_='jsx-2021336621')

    for card in cards:
        if card.find_all("h2", class_='jsx-2021336621 name'):
            laptop_desc = card.find('h2', class_='jsx-2021336621 name').text
            laptop_price = card.find('div', class_='jsx-2021336621').text

            laptops.append((laptop_desc, laptop_price))
            # print('Description:', laptop_desc)
            # print('Price:', laptop_price)
            # print('-'*20)

my_data = pd.DataFrame(laptops, columns=['Description', 'Price'])

try:
    my_data.to_excel(res_file, encoding='utf8')
    print(f'Successfully saved to {res_file}')
except Exception as e:
    print('Failed to save results')
    print(e)
