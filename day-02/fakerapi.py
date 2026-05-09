import requests

api_url = "https://fakerapi.it/api/v2/addresses?_quantity=1"



response = requests.get(url=api_url)

for key,value in response.json().items():
    print(key,value)
