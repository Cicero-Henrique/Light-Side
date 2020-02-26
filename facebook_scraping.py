from mechanize import Browser
from requests import get
from bs4 import BeautifulSoup
import pandas as pd

class facebook_scraping:

    def scraping(url):

        names = []
        titles = []
        contents = []
        others_content = []

        response = get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        study = soup.find_all("div", {"class": "_2lzr _50f5 _50f7"})
        cities = soup.find_all("span", {"class": "_2iel _50f7"})
        table_favorites = soup.find("table", {"class": "mtm _5e7- profileInfoTable _3stp _3stn"})
        all_favorites = table_favorites.find_all("div", {"class": "labelContainer"})
        page_name = table_favorites.find_all("div", {"class": "mediaPageName"})
        print("Study: " + study[0].a.get_text() + " - " + study[1].a.get_text())
        print("Was born in: " + cities[1].a.get_text() + " - Living in: " + cities[0].a.get_text())
        for i in range(0, len(all_favorites)-1):
            titles.append(all_favorites[i].get_text())
            contents.append(page_name[i].get_text())
            print(titles[i] + ": " + contents[i])

        others_title = all_favorites[len(all_favorites) -1].get_text()
        others_content_visible = table_favorites.find_all("span", {"class": "visible"})
        others_content_visible = others_content_visible[0].find_all("a")
        others_content_hidden = table_favorites.find_all("span", {"class": "hiddenItem"})
        others_content_hidden = others_content_hidden[0].find_all("a")

        for i in range(0, len(others_content_visible)):
            others_content.append(others_content_visible[i].get_text())

        for i in range(0, len(others_content_hidden)):
            others_content.append(others_content_hidden[i].get_text())

        others_content.sort()

        def my_range(start, end, step):
            while start <= end:
                yield start
                start += step

        for i in range(0, len(others_content)):
            if(i%2 == 0):
                if((i+1 < len(others_content))):
                    print('{0:50}  {1}'.format(others_content[i], others_content[i+1]))
                else:
                    print(others_content[i])