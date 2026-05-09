import requests 

api_url = "https://fakerapi.it/api/v2/persons?_quantity=1&_gender=female&_birthday_start=2005-01-01"

response = requests.get(url=api_url)

data = response.json()

try:
    print(data["local"])
except KeyError:
    print("Key not found")
