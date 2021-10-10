import requests

# Start request
response = requests.get('https://google.com')

# Status
print(response.status_code)

# Response type
print(response.headers['content-type'])

# Response content
# print(response.content)
print(response.text)

# Save content in a file
with open('google.html', 'w') as f:
    f.write(response.text)
