import requests
import time
import webbrowser

url = 'https://google.com'
for i in range(3):
    try:
        response = requests.get(url, timeout=3)
        print(f'try {i+1}: Success')
        webbrowser.open_new(url)
        break
    except: 
        print(f'try {i+1}: Failed')
    
    time.sleep(3)         
