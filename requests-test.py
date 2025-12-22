import requests

url = 'https://gutendex.com/books/'
response = requests.get(url)
data = response.json()
print(data['results'][0]['title'])
