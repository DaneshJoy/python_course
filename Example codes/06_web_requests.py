import requests

url = "https://weatherapi-com.p.rapidapi.com/current.json"

city = input('Enter the name of your city: ')
querystring = {"q": city}

# Put your rapidapi key here
headers = {
    'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
    'x-rapidapi-key': "YOUR RAPIDAPI KEY"
    }

response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:
    # print(response.text)
    print(response.reason)
    res_json = response.json()
    print(f"Current Temprature: {res_json['current']['temp_c']} ^C")
    print(f"Current Condition: {res_json['current']['condition']['text']}")
else:
    print(response.reason)
