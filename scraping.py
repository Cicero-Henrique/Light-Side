from mechanize import Browser
from requests import get
from bs4 import BeautifulSoup
import pandas as pd


class Scraping:

    def scraping(url):

        names = []
        titles = []
        contents = []
        favorites = []

        profile = {}

        response = get(url)

        soup = BeautifulSoup(response.text, 'html.parser')

        name = soup.find("div", {"class": "_2nlj _2xc6"})
        name = name.find("a")
        name = name.get_text()
        print(name)
        profile["name"] = name

        info = soup.find_all("div", {"class": "_4qm1"})
        labels = soup.find_all("div", {"class": "clearfix _h71"})
        for i in range(0, len(labels)):
            label = labels[i].get_text()
            if(label.lower() == "trabalho"):
                print("\t\t " + str(i) + " - " + label)
                work = info[i].find_all("div", {"class": "_2lzr _50f5 _50f7"})
                profile["work"] = []
                for i in range(0, len(work)):
                    print(work[i].a.get_text())
                    profile["work"].append(work[i].a.get_text())

            if(label.lower() == "educação"):
                print("\t\t " + str(i) + " - " + label)
                study = info[i].find_all("div", {"class": "_2lzr _50f5 _50f7"})
                profile["study"] = []
                for i in range(0, len(study)):
                    print(study[i].a.get_text())
                    profile["study"].append(study[i].a.get_text())

            if(label.lower() == "cidade atual e cidade natal"):
                print("\t\t " + str(i) + " - " + label)
                cities = info[i].find_all("span", {"class": "_2iel _50f7"})
                profile["cities"] = []
                for i in range(0, len(cities)):
                    print(cities[i].a.get_text())
                    profile["cities"].append(cities[i].a.get_text())

        try:
            table_favorites = soup.find(
                "table", {"class": "mtm _5e7- profileInfoTable _3stp _3stn"})
            all_favorites = table_favorites.find_all(
                "div", {"class": "labelContainer"})
            page_name = table_favorites.find_all(
                "div", {"class": "mediaPageName"})

            for i in range(0, len(all_favorites) - 1):
                titles.append(all_favorites[i].get_text())
                contents.append(page_name[i].get_text())
                print(titles[i] + ": " + contents[i])

            others_title = all_favorites[len(all_favorites) - 1].get_text()
            others_content_visible = table_favorites.find_all(
                "span", {"class": "visible"})
            others_content_visible = others_content_visible[0].find_all("a")
            others_content_hidden = table_favorites.find_all(
                "span", {"class": "hiddenItem"})
            others_content_hidden = others_content_hidden[0].find_all("a")

            for i in range(0, len(others_content_visible)):
                favorites.append(others_content_visible[i].get_text())

            for i in range(0, len(others_content_hidden)):
                favorites.append(others_content_hidden[i].get_text())

            profile["words"] = favorites.sort()

        except BaseException:
            profile["words"] = []

        def my_range(start, end, step):
            while start <= end:
                yield start
                start += step

        profile["words"] = favorites

        return profile
