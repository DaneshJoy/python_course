import requests

''' Get current weather '''
url = "https://weatherapi-com.p.rapidapi.com/current.json"

city = input('Enter the name of your city: ')
querystring = {"q": city}

# Put your rapidapi key here
headers = {
    'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
    'x-rapidapi-key': "a0f483e62cmsh0637ffc253b3c09p195f4fjsnd20f60deec03"
    }

response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:
    # print(response.text)
    print("Status:", response.reason)
    res_json = response.json()
    print(f"Current Temprature: {res_json['current']['temp_c']} ^C")
    print(f"Current Condition: {res_json['current']['condition']['text']}")
else:
    print("Status:", response.reason)
    
    
''' Get weather forecast '''
url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

days = 3
querystring = {"q":city, "days":days}

headers = {
    "X-RapidAPI-Key": "a0f483e62cmsh0637ffc253b3c09p195f4fjsnd20f60deec03",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print("-"*30)
print("Weather forecast for next 3 days")
if response.status_code == 200:
    # print(response.text)
    print("Status:", response.reason)
    res_json = response.json()
    for i in range(days):
        print(f"Max Temprature for day {i+1}: {res_json['forecast']['forecastday'][i]['day']['maxtemp_c']}")

else:
    print("Status:", response.reason)
