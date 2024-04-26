IMDB Web Scraper

<!-- ![Design preview for the Space tourism website coding challenge](./preview.jpg) -->

## Welcome! 👋

Challenges help you improve your coding skills by building realistic projects. This challenges is a perfect portfolio pieces, so please feel free to use what you create in your portfolio to show others.

**To do this challenge, you need a strong understanding of Python**

## Understanding my project
from bs4 import BeautifulSoup
import requests, openpyxl
import time

#  To create a new Excel sheet with openpyxl
excel = openpyxl.Workbook()
print(excel.sheetnames)  # To see how many sheet the Excel file has
sheet = excel.active  # To make sure you're working on the active sheet
sheet.title = 'Top Rated Movies'  # Changed the name of the sheet
print(excel.sheetnames)

try:
    #  Fix for - 403 Client Error: Forbidden for url ( indicates that the server understood the request but refuses to authorize it. This typically happens when the server detects that the request is coming from a bot or automated script, rather than a human user)


    #  Add User-Agent Header: Some websites require a User-Agent header in the request to identify the request as coming from a legitimate browser.
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
    }  #  An example of a user agent string for a Windows 10 machine using Chrome

    #  This will access the imdb website and return a response object(html source code)
    source = requests.get('https://www.imdb.com/chart/top/', headers=headers)
    #  Capture and error from the response object
    source.raise_for_status()

    #  Use a Delay: Sometimes, sending too many requests in a short period can trigger a 403 error. You can try adding a delay between requests using the time.sleep function
    time.sleep(2)  # Delay for 2 seconds

    #  Extracting the html source code
    soup = BeautifulSoup(source.text, 'html.parser')

    movies = soup.find('ul', class_="compact-list-view").find_all('li')

    for movie in movies:
        name = movie.find('div', class_="ipc-title").a.text.split('.')[1]
        rank = movie.find('div', class_="ipc-title").get_text(strip=True).split('.')[0]

        '''
        trying = movie.find('div', class_="sc-b189961a-7").text  
        # This will print out the text in the divs.
        # This also does the same thing with the line below but with less accuracy
        '''

        year = movie.find('span', class_="sc-b189961a-8").text
        # This will print out the content of all the spans

        rating = movie.find('span', class_="ipc-rating-star").text

        # print(name)
        # print(rank)
        # print(trying)
        # print(year)
        # print(rating)

        print(rank, name, year, rating)
        sheet.append(rank, name, year, rating)  # Loads it inot the excel file

    print(len(movies)) 
    # Prints out the length of the movie items

except Exception as e:
    print(e)

excel.save('IMDB Movies Ratings.xlsx')  # This saves the content of the scrapping into the excel sheet

## Building your project
<!-- Feel free to use any workflow that you feel comfortable with. Below is a suggested process, but do not feel like you need to follow these steps:

1. Separate the `starter-code` from the rest of this project and rename it to something meaningful for you. Initialize the codebase as a public repository on [GitHub](https://github.com/). Creating a repo will make it easier to share your code with the community if you need help. If you're not sure how to do this, [have a read-through of this Try Git resource](https://try.github.io/).
2. Configure your repository to publish your code to a web address. This will also be useful if you need some help during a challenge as you can share the URL for your project with your repo URL. There are a number of ways to do this, and we provide some recommendations below.
3. Look through the workflow to start planning out how you'll tackle the project. This step is crucial to help you think ahead for task.
4. Before adding any styles, structure your content with HTML. Writing your HTML first can help focus your attention on creating well-structured content.
5. Write out the base styles for your project, including general content styles, such as `font-family` and `font-size`.
6. Start adding styles to the top of the page and work down. Only move on to the next section once you're happy you've completed the area you're working on. -->

<!-- ## Deploying your project

As mentioned above, there are many ways to host your project for free. Our recommend hosts are:

- [GitHub Pages](https://pages.github.com/)
- [Vercel](https://vercel.com/)
- [Netlify](https://www.netlify.com/) -->


**Have fun building!** 🚀
