import os
from word import Word
from combinations import Combinations
from wordlist_generator import WordlistGenerator as wg
from validate import Validate
from view import View as view

class generate_passwords:

    def validate_date(self, date):
        if(int(date[0:2]) > 31):
            return False
        if(int(date[2:4]) > 12):
            return False
        if(int(date[4:]) < 1900 or int(date[4:]) > 2020):
            return False
        if(date[2:4] == "02" and int(date[0:2]) > 29):
            return False
        return True

    def get_birthday(self):
        birthday = input("\t\t Birthday (DDMMYYYY): ")
        if(birthday == ''):
            return birthday
        valid = self.validate_date(birthday)
        while len(birthday) != 8 or not birthday.isdigit() or not valid:
            print("\r\n[-] You must enter 8 digits for birthday!")
            birthday = input("> Birthday (DDMMYYYY): ")
            valid = self.validate_date(birthday)
        return str(birthday)

    def get_information(self, profile):

        profile["victim_nickname"] = input("\t\t Nickname: ").lower()
        profile["victim_birthdate"] = self.get_birthday()

        print("\n\n")
        profile["wife_name"] = input("\t\t Partners name: ").lower()
        profile["wife_nickname"] = input("\t\t Partners nickname: ").lower()
        profile["wife_birthdate"] = self.get_birthday()

        childs = True
        profile["kids"] = []
        while(childs is True):
            print("\n\n")
            kid = {
                "name" : input("\t\t Child's name: ").lower(),
                "nickname" : input("\t\t Child's nickname: ").lower(),
                "birthdate" : self.get_birthday()
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
        except:
            add = True
            profile["work"] = []
            while(add):
                work = input("> Where you work or worked: ").lower()
                if(work == ""):
                    add = False
                else:
                    profile["work"].append(work)
                    answer = input("> Do you want add other work? Y/[N]").lower()
                    if(answer == "y"):
                        add = True
                    else:
                        add = False

        try:
            profile["study"]
        except:
            add = True
            profile["study"] = []
            while(add):
                study = input("> Where you study or studied: ").lower()
                if(study == ""):
                    add = False
                else:
                    profile["study"].append(study)
                    answer = input("> Do you want add other school or university? Y/[N]").lower()
                    if(answer == "y"):
                        add = True
                    else:
                        add = False

        try:
            profile["cities"]
        except:
            add = True
            profile["cities"] = []
            while(add):
                city = input("> What city are you living? ").lower()
                if(city == ""):
                    add = False
                else:
                    profile["cities"].append(city)
                    answer = input("> Do you want add other city as your hometown? Y/[N]").lower()
                    if(answer == "y"):
                        add = True
                    else:
                        add = False

        print("\r\n")

        answer = input("> Do you want to add some extra words? Y/[N]: ").lower()
        if(answer == 'y'):
            answer = input("> Insert all words separated by ',' : ").lower()
            profile["extra_info"] = answer
        else:
            profile["extra_info"] = False

        return profile

    def write_in_file(self, all_combinations):
        f = open('wordlist.txt', 'w', encoding='utf8')
        for word in all_combinations:
            if(type(word) is list):
                for word2 in word:
                    f.write(word2 + "\n")
            else:
                f.write(word + "\n")
        f.close()

    def menu(self):
        op = 4
        while op != '1' and op != '2' and op != '3':
            print('\t\t MENU')
            print('1- Generate wordlist')
            print('2- Validate password')
            print('3- Close')
            op = input('What is your choice number: ')
        return op



    def __init__(self, profile):
        self.get_information(profile)
        view.clear()
        view.show_info(profile)
        finish = False
        t = Combinations(profile)
        info = t.info

        while (not finish):
            op = self.menu()
            if(op == '1'):
                wg(info)
                # combinations = teste.combinations
                # self.write_in_file(combinations)

            elif (op == '2'):
                Validate(info)

            else:
                try:
                    os.remove("wordlist.txt")
                    finish = True

                except:
                    finish = True

        # Show the most obvious passwords combinations. E.g.: Combinations between name and nick, name and birthdate, name and wife name, pet company
        # Hide the less obvious passwords combinations. E.g.: Combinations based in social media

        # Be sure that all info is being used
        # Improve the scraping
        # Reduce the code
        # Separate in modules

        # Name
        #   Work
        #   Study
        #   City was born and living
        # Likes

        # Victim nickname
        # Victim birthday
        # Wife name
        # Wife nickname
        # Wife birthday
        #     Kids names
        #     Kids nicknames
        #     Kids birthdays
