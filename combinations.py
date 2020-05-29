class Combinations:

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
            combinations.append(self.generate_names(kid["name"], kid["nickname"]))

        return combinations

    def generate_kids_birthdays(self, kids):
        combinations = []
        for kid in kids:
            combinations.append(self.generate_birthdates_combinations(kid["birthdate"]))

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

        if(not date.isdigit()):
            return combinations

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

    def prepare_extra_info(self, info):
        combinations = []
        combinations = info.split(",")
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

    def prepare_words(self, array_likes):
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

    def get_info(self, info):
        return info

    def __init__(self, profile):

        names = {
            "victim_names": self.generate_names(profile["name"], profile["victim_nickname"]),
            "wife_names": self.generate_names(profile["wife_name"], profile["wife_nickname"]),
            "kid_names": self.generate_kids_names(profile["kids"]),
            "pet_names": self.generate_names(profile["pet"], "")
        }
        birthdays = {
            "victim_birthdate_combinations": self.generate_birthdates_combinations(profile["victim_birthdate"]),
            "wife_birthdate_combinations": self.generate_birthdates_combinations(profile["wife_birthdate"]),
            "kid_birthdate_combinations": self.generate_kids_birthdays(profile["kids"])
        }

        names = self.move_to_unique_array(names)
        birthdays = self.move_to_unique_array(birthdays)
        names = self.remove_duplicates(names)
        birthdays = self.remove_duplicates(birthdays)
        names = self.from_dict_to_list(names)
        birthdays = self.from_dict_to_list(birthdays)

        # names_combinations = self.combine_intern_info(names)
        # birthdays_combinations = self.combine_intern_info(birthdays)
        # names_combinations = self.remove_duplicates_array(names_combinations)
        # birthdays_combinations = self.remove_duplicates_array(birthdays_combinations)



        work = self.prepare_words(profile["work"])
        city = self.prepare_words(profile["cities"])
        study = self.prepare_words(profile["study"])
        if(profile["extra_info"]):
            extra_info = self.prepare_words(self.prepare_extra_info(profile["extra_info"]))
        try:
            likes = self.prepare_words(profile["words"])
        except:
            likes = []

        info = {
            "names": names,
            "birthdays": birthdays,
            "likes": likes,
            "city": city,
            "work": work,
            "study": study
        }
        self.info = info
