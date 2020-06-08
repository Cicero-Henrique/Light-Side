import os
from combinations import Combinations
from wordlist_generator import WordlistGenerator as wg
from validate import Validate
from scraping import Scraping as fs
import view
import datetime
import re


def validate_url(url):
    domain = 'https://pt-br.facebook.com/'
    return ((url.find(domain) == 0) or url == '')


def get_URL():
    valid = False
    while(not valid):
        view.clear()
        print("\t the The URL must be in this format: https://pt-br.facebook.com/")
        url = input("> Insert the URL of your Facebook: ")
        valid = validate_url(url)
    return url


def get_name():
    valid = False
    while (not valid):
        view.clear()
        name = input("Insert your name and surname: ")
        if(re.match('[a-z\s]*$', name)):
            valid = True
    return name


def validate_date(date):
    if(date == ''):
        return True
    try:
        datetime.datetime.strptime(date, "%d%m%Y")
    except Exception:
        return False

    return True


def get_birthday():
    birthday = input("\t\t Birthday (DDMMYYYY): ")
    valid = validate_date(birthday)
    while not valid:
        print("\r\n[-] You must enter a valid date in 8 digits!")
        birthday = input("> Birthday (DDMMYYYY): ")
        valid = validate_date(birthday)
    return str(birthday)


def get_information(profile):

    profile["victim_nickname"] = input("\t\t Nickname: ").lower()
    profile["victim_birthdate"] = get_birthday()

    print("\n\n")
    profile["wife_name"] = input("\t\t Partners name: ").lower()
    profile["wife_nickname"] = input("\t\t Partners nickname: ").lower()
    profile["wife_birthdate"] = get_birthday()

    childs = True
    profile["kids"] = []
    while(childs is True):
        print("\n\n")
        kid = {
            "name": input("\t\t Child's name: ").lower(),
            "nickname": input("\t\t Child's nickname: ").lower(),
            "birthdate": get_birthday()
        }
        profile["kids"].append(kid)
        childs = input("Do you want more kids Y/N? ").lower()
        if(childs == 'y'):
            childs = True
        else:
            childs = False
        print("\r\n")

    profile["pet"] = input("> Pet's name: ").lower()

    try:
        profile["work"]
    except BaseException:
        add = True
        profile["work"] = []
        while(add):
            work = input("> Where you work or worked: ").lower()
            if(work == ""):
                add = False
            else:
                profile["work"].append(work)
                answer = input(
                    "> Do you want to add another work? Y/[N] ").lower()
                if(answer == "y"):
                    add = True
                else:
                    add = False

    try:
        profile["study"]
    except BaseException:
        add = True
        profile["study"] = []
        while(add):
            study = input("> Where you study or studied: ").lower()
            if(study == ""):
                add = False
            else:
                profile["study"].append(study)
                answer = input(
                    "> Do you want to add another school or university? Y/[N] ").lower()
                if(answer == "y"):
                    add = True
                else:
                    add = False

    try:
        profile["cities"]
    except BaseException:
        add = True
        profile["cities"] = []
        while(add):
            city = input("> What city are you living? ").lower()
            if(city == ""):
                add = False
            else:
                profile["cities"].append(city)
                answer = input(
                    "> Do you want to add another city as your hometown? Y/[N] ").lower()
                if(answer == "y"):
                    add = True
                else:
                    add = False

    print("\r\n")

    answer = input(
        "> Do you want to add some extra words? Y/[N]: ").lower()
    if(answer == 'y'):
        answer = input("> Insert all words separated by ',' : ").lower()
        profile["extra_info"] = answer
    else:
        profile["extra_info"] = False

    return profile


def write_in_file(all_combinations):
    try:
        f = open('wordlist.txt', 'w', encoding='utf8')
        for word in all_combinations:
            if(isinstance(word, list)):
                for word2 in word:
                    f.write(word2 + "\n")
            else:
                f.write(word + "\n")
    finally:
        f.close()


def menu():
    op = 4
    while op != '1' and op != '2' and op != '3':
        # view.clear()
        print('\n\t\t MENU')
        print('1- Generate wordlist')
        print('2- Validate password')
        print('3- Close')
        op = input('What is your choice number: ')
    return op


if __name__ == "__main__":

    url = get_URL()
    profile = {}
    if(url != ''):
        profile = fs.scraping(url)
    else:
        profile["name"] = get_name()
    get_information(profile)
    view.clear()
    view.show_info(profile)
    finish = False
    t = Combinations(profile)
    info = t.info

    while (not finish):
        op = menu()
        if(op == '1'):
            wg(info, profile)

        elif (op == '2'):
            Validate(info)

        else:
            try:
                os.remove("wordlist.txt")

            finally:
                finish = True
