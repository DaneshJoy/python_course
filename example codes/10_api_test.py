
import requests

# Test
response1 = requests.post('https://httpbin.org/post',
                          data={'name': 'ali'})
# print(response2.text)
print(response1.headers['content-type'])
response1_json = response1.json()

# Weather
response2 = requests.get('https://www.metaweather.com/api/location/44418/')
print(response2.headers['content-type'])
response2_json = response2.json()
print(response2_json['consolidated_weather'][0])


# # Avatar image
sprites = 'human'
seed = 'mine'
response3 = requests.get(
    f'https://avatars.dicebear.com/api/{sprites}/{seed}.svg',
    params={'mood[]': 'happy'})
print(response3.headers['content-type'])

with open('test.svg', 'w') as f:
    f.write(response3.text)
