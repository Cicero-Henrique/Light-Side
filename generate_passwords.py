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

    def combinations_reverse(self, words):
        combinations = []
        for word in words:
            if(type(word) is list):
                for aux in word:
                    combinations.append(aux[::-1])
            else:
                combinations.append(word[::-1])

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

    def generate_words_combinations_with_special_chars(self, fword, sword):
        chars = ['"""', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':',
                    ';', '<', '=', '>', '?', '@', '[', '"\"', ']', '^', '_', '`', '{', '|', '}', '~']
        combinations = []

        for char in chars:
            combinations.append(fword + sword + char)
            combinations.append(char + fword + sword)
            combinations.append(fword + char + sword)

        return combinations

    def generate_words_combinations(self, first_word, second_word):
        combinations = []

        combinations.append(first_word + second_word)
        combinations.append(self.generate_words_combinations_with_special_chars(first_word, second_word))

        return combinations

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

    def combine_intern_info(self, words):
        combinations = []
        for key1 in words:
            for key2 in words:
                combinations = combinations + self.generate_words_combinations(key1, key2)

        return combinations

    def combine_likes(self, array_likes):
        combinations = []
        for like in array_likes:
            combinations.append(self.remove_articles(like))

        return combinations

    def from_dict_to_list(self, dict1, dict2):
        unique = []
        for arr in dict1.values():
            unique = unique + arr
        
        for arr in dict2.values():
            unique = unique + arr
        
        return unique

    def __init__(self, profile):
        # self.get_information(profile)
        all_combinations = []

        victim_names = self.generate_names(profile["name"][0], profile["victim_nickname"][0])
        victim_birthdate_combinations = self.generate_birthdates_combinations(profile["victim_birthdate"][0])

        wife_names = self.generate_names(profile["wife_name"][0], profile["wife_nickname"][0])
        wife_birthdate_combinations = self.generate_birthdates_combinations(profile["wife_birthdate"][0])

        kid_names = self.generate_names(profile["kid_name"][0], profile["kid_nickname"][0])
        kid_birthdate_combinations = self.generate_birthdates_combinations(profile["kid_birthdate"][0])

        pet_names = self.generate_names(profile["pet"][0], "")
        company_names = self.generate_names(profile["company"][0], "")

        print()
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
        # all_names = self.remove_duplicates(all_names)
        # all_birthdates = self.remove_duplicates(all_birthdates)

        likes = self.combine_likes(profile["words"])

        all_intern_info = self.from_dict_to_list(all_names, all_birthdates)
        
        basewords = all_intern_info + likes
        basewords = self.remove_duplicates_array(basewords)

        all_combinations = self.combine_array(basewords)
        # all_combinations = self.move_to_unique_array(basewords)

        f = open('wordlist.txt', 'w')
        for word in all_combinations:
            if(type(word) is list):
                for word2 in word:
                    f.write(word2 + "\n")
            else:
                f.write(word + "\n")
        f.close()

        # Show the most obvious passwords combinations. E.g.: Combinations between name and nick, name and birthdate, name and wife name, pet company
        # Hide the less obvious passwords combinations. E.g.: Combinations based in social media

        # likes_combinations = self.combine_likes(profile["words"])
        # self.combine_words()
        # self.combine_words_birthdate()
        # self.replace_by_special_chars()

