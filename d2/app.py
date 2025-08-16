import requests

response = requests.get('https://google.com')
print(response.text[:300])  # Выведем первые 100 символов страницы Google