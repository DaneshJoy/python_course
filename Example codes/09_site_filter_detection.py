import requests

site = input('Enter site URL: ')
try:
    resp = requests.get(site, timeout=3)
    if resp.status_code == 200:
        print('This site is available in Iran')
except:
    print('This site is filtered')

