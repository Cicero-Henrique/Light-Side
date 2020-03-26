class generate_passwords:

    def get_information(self, profile):

        profile["victim_nickname"] = input("> Nickname: ").lower()
        birthdate = input("> Birthdate (DDMMYYYY): ")
        while len(birthdate) != 0 and len(birthdate) != 8:
            print("\r\n[-] You must enter 8 digits for birthday!")
            birthdate = input("> Birthdate (DDMMYYYY): ")
        profile["victim_birthdate"] = str(birthdate)

        profile["wife_name"] = input("> Partners) name: ").lower()
        profile["wife_nickname"] = input("> Partners) nickname: ").lower()
        wifeb = input("> Partners) birthdate (DDMMYYYY): ")
        while len(wifeb) != 0 and len(wifeb) != 8:
            print("\r\n[-] You must enter 8 digits for birthday!")
            wifeb = input("> Partners birthdate (DDMMYYYY): ")
        profile["wife_birthdate"] = str(wifeb)
        print("\r\n")

        profile["kid_name"] = input("> Child's name: ").lower()
        profile["kid_nickname"] = input("> Child's nickname: ").lower()
        kidb = input("> Child's birthdate (DDMMYYYY): ")
        while len(kidb) != 0 and len(kidb) != 8:
            print("\r\n[-] You must enter 8 digits for birthday!")
            kidb = input("> Child's birthdate (DDMMYYYY): ")
        profile["kid_birthdate"] = str(kidb)
        print("\r\n")

        profile["pet"] = input("> Pet's name: ").lower()
        profile["company"] = input("> Company name: ").lower()
        print("\r\n")

        answer = input("> Do you want to add special chars at the end of words? Y/[N]: ").lower()
        if(answer == 'y'):
            profile["spechars_validation"] = True
        else:
            profile["spechars_validation"] = False

        answer = input("> Do you want to add some random numbers at the end of words? Y/[N]:").lower()
        if(answer == 'y'):
            profile["randnum"] = True
        else:
            profile["randnum"] = False

        answer = input("> Leet mode? (i.e. leet = 1337) Y/[N]: ").lower()
        if(answer == 'y'):
            profile["leetmode"] = True
        else:
            profile["leetmode"] = False

        return profile

    def combinations_cases(self, names, case):
        combinations = []

        if(case == "lower"):
            for i in range(0, len(names)):
                names[i] = str(names[i].lowercase())
        elif (case == "upper"):
            for i in range(0, len(names)):
                names[i] = str(names[i].uppercase())
        elif (case == "title"):
            for i in range(0, len(names)):
                names[i] = str(names[i].title())
        else:
            for i in range(0, len(names)):
                names[i] = str(names[i].lowercase())

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

    def generate_names(self, name, nickname):
        names = []
        array_names = name.split(" ")
        array_names = array_names.append(nickname)

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
        if(date[2:] < 10):
            short_day = str(day[0:])
        else:
            short_day = day

        if(date[2:4] < 10):
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

    def remove_articles(self, word):
        new_word = ''
        aux = word.split(" ")
        if(len(aux) != 1):
            return aux
        for i in range(0, len(aux)):
            if(aux[i] != 'a' or 'an' or 'the' or 'of'):
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
        combinations.append(self.generate_words_combinations_with_special_chars(first_word, second_word))

        return combinations

    def combine_arrays(self, arr1, arr2):
        combinations = []
        for word1 in arr1:
            for word2 in arr2:
                combinations.append(self.generate_words_combinations(word1, word2))

        return combinations

    def combine_intern_info(self, names):
        combinations = []
        for first_array_name in names:
            for second_aray_name in names:
                combinations.append(self.combine_arrays(first_array_name, second_aray_name))

        return combinations

    def combine_likes(self, array_likes):
        combinations = []
        for i in range(0, len(array_likes)):
            for j in range(0, len(array_likes)):
                first_like = self.remove_articles(array_likes[i])
                second_like = self.remove_articles(array_likes[j])
                first_like = self.generate_names(first_like, "")
                second_like = self.generate_names(second_like, "")
                combinations.append(self.generate_words_combinations(first_like, second_like))

        return combinations

    def init(self, profile):
        all_combinations = []

        victim_names = self.generate_names(profile["name"], profile["nickname"])
        victim_birthdate_combinations = self.generate_birthdates_combinations(profile["birthdate"])

        wife_names = self.generate_names(profile["wife_name"], profile["wife_nickname"])
        wife_birthdate_combinations = self.generate_birthdates_combinations(profile["wife_birthdate"])

        kid_names = self.generate_names(profile["kid_name"], profile["kid_nickname"])
        kid_birthdate_combinations = self.generate_birthdates_combinations(profile["kid_birthdate"])

        pet_names = self.generate_names(profile["pet"], "")
        company_names = self.generate_names(profile["company"], "")

        all_names = [victim_names, wife_names, kid_names, pet_names, company_names]
        all_birthdates = [victim_birthdate_combinations, wife_birthdate_combinations, kid_birthdate_combinations]
        names_combinations = self.combine_intern_info(all_names)
        birthdays_combinations = self.combine_intern_info(all_birthdates)

        names_birthdays_combinations = self.combine_arrays(all_names, all_birthdates)

        # Show the most obvious passwords combinations. E.g.: Combinations between name and nick, name and birthdate, name and wife name, pet company
        # Hide the less obvious passwords combinaations. E.g.: Combinations based in social media 

        likes_combinations = self.combine_likes(profile["words"])
        self.combine_words()
        self.combine_words_birthdate()
        self.replace_by_special_chars()

    init()
