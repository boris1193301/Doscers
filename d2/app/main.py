import requests
from app.resorce import t

def main():
    response = requests.get('https://google.com')
    print(response)  # Выведем первые 100 символов страницы Google
    t.t1()

if __name__ == '__main__':
    main()