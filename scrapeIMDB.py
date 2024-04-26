from bs4 import BeautifulSoup
import openpyxl
import requests
import time

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Top Rated Movies'
sheet.append(['Movie Rank', 'Movie Name', 'Year of Release', 'IMDB Rating'])

try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
    }
    source = requests.get('https://www.imdb.com/chart/top/', headers=headers)
    source.raise_for_status()

    time.sleep(2)

    soup = BeautifulSoup(source.text, 'html.parser')

    movies = soup.find('ul', class_="compact-list-view").find_all('li')

    for movie in movies:
        name = movie.find('div', class_="ipc-title").a.text.split('.')[1]
        rank = movie.find('div', class_="ipc-title").get_text(strip=True).split('.')[0]
        year = movie.find('span', class_="sc-b189961a-8").text
        rating = movie.find('span', class_="ipc-rating-star").text

        print(rank, name, year, rating)
        print("Done...")
        sheet.append([rank, name, year, rating])

except Exception as e:
    print(e)

excel.save('IMDB Movies Ratings.xlsx')
