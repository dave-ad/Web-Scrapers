from bs4 import BeautifulSoup
import requests
import time

try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
    }
    source = requests.get('https://www.imdb.com/chart/top/', headers=headers)
    source.raise_for_status()

    time.sleep(2)  # Delay for 2 seconds

    soup = BeautifulSoup(source.text, 'html.parser')

    movies = soup.find('ul', class_="compact-list-view").find_all('li')

    for movie in movies:
        name = movie.find('div', class_="ipc-title").a.text
        print(name)
        break

    # print(len(movies))

except Exception as e:
    print(e)
