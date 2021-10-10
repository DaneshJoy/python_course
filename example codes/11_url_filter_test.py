
# Check if url is filtered or not

import requests

try:
    response = requests.get('https://facebook.com', timeout=2)
except Exception as e:
    print('Request Timeout')
