import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


my_word = 'UseR'
num_pages = 15
results = []

# %% Get site data
for i in tqdm(range(1, num_pages+1)):
    # Method 1 (only if we don't use tqdm)
    # print(f'--->> Processing Page {i}...')
    res = requests.get(f'https://news.ycombinator.com/news?p={i}')

    # %% Create soup and get specific tags with specific class
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup.prettify())
    
    links = soup.find_all('a', class_='titlelink')
    
    # %% Find our desired word in link texts
    for link in links:
        if my_word.lower() in link.text.lower():
            results.append((link['href'], link.text))
