import requests

url = "https://weatherapi-com.p.rapidapi.com/current.json"

city = input('Enter the name of your city: ')
querystring = {"q": city}

headers = {
    'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
    'x-rapidapi-key': "cdd069ee3emsh2881e053f53fdf0p1bafd9jsn2efdaeb7d08a"
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
