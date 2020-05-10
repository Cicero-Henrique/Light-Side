import os

class generate_passwords:

    def get_birthday(self):
        birthday = input("\t\t Birthday (DDMMYYYY): ")
        while len(birthday) != 8 and birthday.isdigit():
            print("\r\n[-] You must enter 8 digits for birthday!")
            birthday = input("> Birthday (DDMMYYYY): ")
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

        answer = input("> Do you want to add special chars at the end of words? Y/[N]: ").lower()
        if(answer == 'y'):
            profile["spechars_validation"] = True
        else:
            profile["spechars_validation"] = False

        return profile

    def contains_list(self, combinations):
        for i in combinations:
            if(type(i) is list):
                return True
        return False

    def remove_duplicates(self, dictionary):

        for key in dictionary:
            duplicates = []
            [duplicates.append(item) for item in dictionary[key] if item not in duplicates]
            dictionary[key] = duplicates

        return dictionary

    def remove_duplicates_array(self, array):

        duplicates = []
        [duplicates.append(item) for item in array if item not in duplicates]
        return duplicates

    def move_to_unique_array(self, names):

        for key in names:
            uniqueArray = False
            while(uniqueArray is False):
                external_words = [x for x in names[key] if type(x) is str]
                internal_words = [x for x in names[key] if type(x) is list]
                final = [j for i in internal_words for j in i]

                names[key] = final + external_words
                if( self.contains_list(names[key]) is False):
                    uniqueArray = True

        return names

    def combinations_cases(self, names, case):
        combinations = []

        if(case == "lower"):
            for word in names:
                combinations.append(str(word.lower()))
        elif (case == "upper"):
            for word in names:
                combinations.append(str(word.upper()))
        elif (case == "title"):
            for word in names:
                combinations.append(str(word.title()))
        else:
            for word in names:
                combinations.append(str(word.lower()))

            for i in range(0, len(names)):
                for j in range(0, len(names)):
                    combinations.append(names[i] + names[j].title())

        return combinations

        for i in range(0, len(names)):
            for j in range(0, len(names)):
                combinations.append(names[i] + names[j])

        return combinations

    def combinations_reverse(self, words):
        combinations = []
        for word in words:
            combinations.append(word[::-1])

        return combinations

    def generate_kids_names(self, kids):
        combinations = []
        for kid in kids:
            combinations.append(self.generate_names(kid.name, kid.nickname))

        return combinations

    def generate_kids_birthdays(self, kids):
        combinations = []
        for kid in kids:
            combinations.append(self.generate_birthdates_combinations(kid.birthday))

        return combinations

    def generate_names(self, name, nickname):
        names = []
        array_names = name.split()
        array_names.append(nickname)

        for aux in array_names:
            names.append(aux)
        names.append(self.combinations_cases(array_names, "lower"))
        names.append(self.combinations_cases(array_names, "upper"))
        names.append(self.combinations_cases(array_names, "title"))
        names.append(self.combinations_cases(array_names, "camel"))
        names.append(self.combinations_reverse(names))

        return names

    def generate_birthdates_combinations(self, date):
        combinations = []

        day = str(date[2:])
        month = str(date[2:4])
        year = str(date[:4])
        short_year = str(year[1:])
        if(int(date[2:]) < 10):
            short_day = str(day[0:])
        else:
            short_day = day

        if(int(date[2:4]) < 10):
            short_month = str(month[0:])
        else:
            short_month = month

        combinations.append(date)                                       # normal
        combinations.append(day)                                        # day
        combinations.append(month)                                      # month
        combinations.append(year)                                       # year
        combinations.append(date[::-1])                                 # reverse
        combinations.append(month+day+year)                             # MMDDYYYY
        combinations.append(day + month + short_year)                   # DDMMYY
        combinations.append(month + day + short_year)                   # MMDDYY
        combinations.append(short_day + short_month + short_year)       # DMYY
        combinations.append(short_month + short_day + short_year)       # MDYY
        combinations.append(short_day + short_month + year)             # DMYYYY
        combinations.append(short_month + short_day + year)             # MDYYYY
        return combinations

    def combination_names_birthdates(self, birthdates, names):
        combinations = []
        for name in names:
            for birthdate in birthdates:
                combinations.append(name + birthdate)
                combinations.append(birthdate + name)
                if(" " in name):
                    aux = name.split()
                    word = ""
                    for i in range(0, len(aux)-1):
                        word = word + aux[i] + birthdate
                    combinations.append(word)
        return combinations

    def generate_likes(self, likes):
        combinations = []
        combinations.append(self.combinations_cases(likes, "lower"))
        combinations.append(self.combinations_cases(likes, "upper"))
        combinations.append(self.combinations_cases(likes, "title"))
        combinations.append(self.combinations_reverse(combinations))

        return combinations

    def remove_articles(self, word):
        new_word = ''
        aux = word.split(" ")
        if(len(aux) == 1):
            return word.title()
        for i in range(0, len(aux)):
            if(aux[i] != 'a' or 'an' or 'the'):
                if(aux[i].isdigit() == True):
                    new_word = new_word + str(aux[i])
                else:
                    new_word = new_word + aux[i].title()

        return new_word

    def generate_words_combinations_with_special_chars(self, first_array, second_array):
        chars = ['"""', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':',
                    ';', '<', '=', '>', '?', '@', '[', '"\"', ']', '^', '_', '`', '{', '|', '}', '~']
        combinations = []

        for fword in first_array:
            for sword in second_array:
                for char in chars:
                    combinations.append(fword + sword + char)
                    combinations.append(char + fword + sword)
                    combinations.append(fword + char + sword)

                    combinations.append(sword + fword + char)
                    combinations.append(char + sword + fword)
                    combinations.append(sword + char + fword)

        return combinations

    def generate_words_combinations(self, first_word, second_word):
        combinations = []

        combinations.append(first_word + second_word)
        combinations.append(second_word + first_word)
        # combinations.append(self.generate_words_combinations_with_special_chars(first_word, second_word))

        return combinations

    def combine_arrays(self, arr1, arr2):
        combinations = []
        for word1 in arr1:
            for word2 in arr2:
                combinations = combinations + self.generate_words_combinations(word1, word2)

        return combinations

    def combine_intern_info(self, dictionary):
        combinations = []
        for key1 in dictionary:
            for key2 in dictionary:
                combinations = combinations + self.combine_arrays(dictionary[key1], dictionary[key2])

        return combinations

    def combine_likes(self, array_likes):
        combinations = []
        for like in array_likes:
            combinations.append(self.remove_articles(like))

        return combinations

    def from_dict_to_list(self, dict1):
        unique = []
        for arr in dict1.values():
            unique = unique + arr

        return unique

    def combine_array(self, arr):
        combinations = []
        i = 0
        for word1 in arr:
            i = i + 1
            j = 0
            for word2 in arr:
                j = j + 1
                print(str(i) + "/" + str(len(arr)) + "\t\t"+ str(j) + "/" + str(len(arr)))
                combinations = combinations + self.generate_words_combinations(word1, word2)

        return combinations

    def write_in_file(self, all_combinations):
        f = open('wordlist.txt', 'w', encoding='utf8')
        for word in all_combinations:
            if(type(word) is list):
                for word2 in word:
                    f.write(word2 + "\n")
            else:
                f.write(word + "\n")
        f.close()

    def write_and_replace(self, all_combinations):
        f = open('wordlist.txt', 'w')
        for word in all_combinations:
            f.write(word + '\n')
            f.write(self.replace_by_spec_chars(word) + '\n')
        f.close()

    def replace_by_spec_chars(self, word):
        replaced = ''
        word = word.lower()
        if('a' in word):
            replaced = word.replace('a', '@')
            #combinations.append(replaced)
        if('e' in word):
            replaced = replaced.replace('e', '3')

            # combinations.append(word.replace('e', '3'))
            # combinations.append(replaced)
        if('o' in word):
            replaced = replaced.replace('o', '0')

            # combinations.append(word.replace('o', '0'))
            # combinations.append(replaced)
        if('s' in word):
            replaced = replaced.replace('s', '5')

            # combinations.append(word.replace('s', '5'))
            # combinations.append(replaced)
        if('i' in word):
            replaced = replaced.replace('i', '!')
            # combinations.append(word.replace('i', '!'))
            # combinations.append(replaced)

            replaced = replaced.replace('!', '1')
            # combinations.append(word.replace('!', '1'))
            # combinations.append(replaced)

        return replaced

    def get_level(self):
        print("Choose the level of combinations: ")
        print("1- Soft")
        print("2- Intermediate")
        print("3- Intense")
        x = 4
        while(int(x) > 3 or int(x) < 1):
            x = input("What you prefer? ")
        return int(x)

    def first_look(self, word):
        chars = ['"""', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':',
                    ';', '<', '=', '>', '?', '@', '[', '"\"', ']', '^', '_', '`', '{', '|', '}', '~']
        contains_digit = False
        contains_spec_char = False
        if(len(word) < 8):
            print("Your password is weak because it's too short!")
            return True

        for character in word:
            if character.isdigit():
                contains_digit = True
            if(character in chars):
                contains_spec_char = True
            if contains_digit and contains_spec_char:
                break

        if(not contains_digit):
            print("Your password is weak because it not contains any number!")
            return True

        if(not contains_spec_char):
            print("Warning! Consider using special characters.")

        return False

    def is_weak(self, data):
        password = input("What is the password to validate: ")
        weak = self.first_look(password)
        if(not weak):
            for word in data:
                if word.lower() in password.lower() and word != '':
                    weak = True
                    print("Your password is weak, I found " + word + " in your profile.")
                    return weak

        return weak

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
        finish = False
        while (not finish):
            op = self.menu()
            all_combinations = []

            victim_names = self.generate_names(profile["name"], profile["victim_nickname"])
            victim_birthdate_combinations = self.generate_birthdates_combinations(profile["victim_birthdate"])

            wife_names = self.generate_names(profile["wife_name"], profile["wife_nickname"])
            wife_birthdate_combinations = self.generate_birthdates_combinations(profile["wife_birthdate"])

            kid_names = self.generate_kids_names(profile["kids"])
            kid_birthdate_combinations = self.generate_kids_birthdays(profile["kid_birthdate"])

            pet_names = self.generate_names(profile["pet"], "")
            company_names = self.generate_names(profile["company"], "")

            all_names = {
                "victim_names": victim_names,
                "wife_names": wife_names,
                "kid_names": kid_names,
                "pet_names": pet_names,
                "company_names": company_names
            }
            all_birthdates = {
                "victim_birthdate_combinations": victim_birthdate_combinations,
                "wife_birthdate_combinations": wife_birthdate_combinations,
                "kid_birthdate_combinations": kid_birthdate_combinations
            }
            all_names = self.move_to_unique_array(all_names)
            all_birthdates = self.move_to_unique_array(all_birthdates)
            all_names = self.remove_duplicates(all_names)
            all_birthdates = self.remove_duplicates(all_birthdates)

            names_combinations = self.combine_intern_info(all_names)
            birthdays_combinations = self.combine_intern_info(all_birthdates)
            names_combinations = self.remove_duplicates_array(names_combinations)
            birthdays_combinations = self.remove_duplicates_array(birthdays_combinations)

            likes = self.combine_likes(profile["words"])
            all_intern_info = self.from_dict_to_list(all_names)
            all_intern_info = all_intern_info + self.from_dict_to_list(all_birthdates)

            if(int(op) == 1):
                profile["level"] = self.get_level()
                if(profile["level"] == 1):
                    basewords = all_intern_info + likes
                elif(profile["level"] == 2):
                    base_likes = self.generate_likes(likes)
                    all_likes = {
                        "lower": base_likes[0],
                        "tile": base_likes[2],
                        "camel": likes
                    }

                    basewords = all_intern_info + self.from_dict_to_list(all_likes)
                else:
                    names_birthdays = self.combination_names_birthdates(all_birthdates, all_names)
                    likes_birthdays = self.combination_names_birthdates(likes, all_names)
                    basewords = all_intern_info + names_birthdays + likes_birthdays

                basewords = self.remove_duplicates_array(basewords)
                all_combinations = self.combine_array(basewords)

                profile["spechars_validation"] = False
                if(profile["spechars_validation"]):
                    all_combinations = self.move_to_unique_array_final(all_combinations)
                    self.write_and_replace(all_combinations)
                else:
                    self.write_in_file(all_combinations)
                self.write_in_file(all_combinations)

            elif op == '2':
                all_intern_info = self.remove_duplicates_array(all_intern_info)
                want_finish = False
                while not want_finish:
                    if (not self.is_weak(all_intern_info)):
                        print("Congratulations, this passwords looks fine.")
                    op = "C"
                    while (op.lower() != 'n' or op.lower() != 'y'):
                        op = input("Do you want to try another password? Y/N ")
                        if(op.lower() == 'n' or op.lower() == 'y'):
                            break
                    if(op.lower() == "n"):
                        want_finish = True

            else:
                os.remove("wordlist.txt")
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
