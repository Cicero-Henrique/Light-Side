import os

class View:

    def clear():
        clear = lambda: os.system('cls')

    def show_info(profile):
        print("Name: {0:10}  {1}".format(profile["name"], profile["wife_name"]))
        print("Nickname: {0:10}  {1}".format(profile["victim_nickname"], profile["wife_nickname"]))
        print("Birthday: {0:10}  {1}".format(profile["victim_birthdate"], profile["wife_birthdate"]))

        print("\n\n")
        print("\r Kids")
        for kid in profile["kids"]:
            print("Name: {}".format(kid["name"]))
            print("Nickname: {}".format(kid["nickname"]))
            print("Birthday: {}".format(kid["birthdate"]))

        print("\n Pet:{}".format(profile["pet"]))

        print("\n\n")
        print("\r Works")
        for work in profile["work"]:
            print(work)

        print("\n\n")
        print("\r Study")
        for study in profile["study"]:
            print(study)

        print("\n\n")
        print("\r Cities")
        for city in profile["cities"]:
            print(city)