import requests

url = "https://yahoo-weather5.p.rapidapi.com/weather"

querystring = {"location": "helsinki", "format": "json", "u": "f"}

headers = {
    "X-RapidAPI-Key": "ad893210cemsh233ed6f812a1039p1693f5jsnb7670945e749",
    "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
