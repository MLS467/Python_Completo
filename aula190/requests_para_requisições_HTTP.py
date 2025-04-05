import requests


# url = "http://localhost:8000/html/"
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

# print(response)
# print(json.dumps(, indent=2))
# print(response.headers)

teste = response.json()

for index, user in enumerate(teste):
    print(index + 1, user["name"])
