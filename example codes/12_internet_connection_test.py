
import requests
import time

for i in range(4):
    try:
        response = requests.get('https://google.com', timeout=2)
        print(f'try {i+1}: Success')
        break
    except Exception as e: 
        print(f'try {i+1}: Failed')
        time.sleep(3)
