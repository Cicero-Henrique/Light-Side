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
    
    def generate_names(self, profile):
        names = []
        array_names = profile["name"].split(" ")


                                        # continuar aqui



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
    
    def generate_names_combinations(self, names):
        combinations = []
        for name in names:
            combinations.append(name[::-1].title())
            name = name.title()
            combinations.append(name)
            name.replace(" ", "")
            combinations.append(name)
            combinations.append(name.uppercase())
            combinations.append(name.lowercase())
            combinations.append(name[::-1])
        
        return combinations

    def combination_birthdates_names(self, birthdates, names):
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
        first_word_combinations = self.generate_names_combinations(first_word)
        second_word_combinations = self.generate_names_combinations(second_word)
        
        for fword in first_word_combinations:
            for sword in second_word_combinations:
                combinations.append(fword + sword)
                combinations.append(sword + fword)
        self.generate_words_combinations_with_special_chars(first_word, second_word)
        
        return combinations

    def combine_likes(self, array_likes):
        combinations = []
        for i in range(0, len(array_likes)):
            for j in range(0, len(array_likes)):
                first_like = self.remove_articles(array_likes[i])
                second_like = self.remove_articles(array_likes[j])
                combinations.append(first_like + second_like)                                   # necessary in caseOf + thisThing happend
                combinations.append(second_like + first_like)                                   # necessary in thisThing + caseOf happend
                combinations.append(self.generate_words_combinations(first_like, second_like))
        
        return combinations

    def init(self, profile):
        all_combinations = []

        victim_names = self.generate_names(profile)

        victim_names_combinations = self.generate_names_combinations(profile["name"], profile["nickname"])
        victim_birthdate_combinations = self.generate_birthdates_combinations(profile["birthdate"])
        victim_names_birthdate_combinations = self.combination_names_birthdates(victim_birthdate_combinations, victim_names_combinations)

        wife_names_combinations = self.generate_names_combinations(profile["wife_name"], profile["wife_nickname"])
        wife_birthdate_combinations = self.generate_birthdates_combinations(profile["wife_birthdate"])
        wife_names_birthdate_combinations = self.combination_names_birthdates(wife_birthdate_combinations, wife_names_combinations)

        kid_names_combinations = self.generate_names_combinations(profile["kid_name"], profile["kid_nickname"])
        kid_birthdate_combinations = self.generate_birthdates_combinations(profile["kid_birthdate"])
        kid_names_birthdate_combinations = self.combination_names_birthdates(kid_birthdate_combinations, kid_names_combinations)

        family_combinations = self.combine_family(
            victim_names_combinations, victim_birthdate_combinations,
            wife_names_combinations, wife_birthdate_combinations,
            kid_names_combinations, kid_names_birthdate_combinations
        )
        
        # wife_names_combinations
        # kid_names_combinations
        # combine_family
        # combine_profile                   pet, company

        # Show the most obvious passwords combinations. E.g.: Combinations between name and nick, name and birthdate, name and wife name, pet company
        # Hide the less obvious passwords combinaations. E.g.: Combinations based in social media 

        all_combinations.append(self.combination_names_birthdates(birthdate_combinations, names_combinations))
        all_combinations.append(self.combine_likes(profile["words"]))
        self.combine_words()
        self.combine_words_birthdate()
        self.replace_by_special_chars()
    
    init()
