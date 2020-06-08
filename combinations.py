from word import Word
import re


class Combinations(Word):

    def contains_list(self, combinations):

        for combination in combinations:
            if(isinstance(combination, list)):
                return True
        return False

    def remove_duplicates(self, dictionary):

        for key in dictionary:
            duplicates = []
            [duplicates.append(item)
             for item in dictionary[key] if item not in duplicates]
            dictionary[key] = duplicates

        return dictionary

    def move_to_unique_array(self, names):

        for key in names:
            uniqueArray = False
            while(uniqueArray is False):
                external_words = [x for x in names[key] if isinstance(x, str)]
                internal_words = [x for x in names[key] if isinstance(x, list)]
                final = [j for i in internal_words for j in i]

                names[key] = final + external_words
                if(self.contains_list(names[key]) is False):
                    uniqueArray = True

        return names

    def combinations_cases(self, names):
        combinations = []
        combinations += self.get_lower(names)
        combinations += self.get_upper(names)
        combinations += self.get_title(names)
        combinations += self.get_camel(names)
        combinations += self.get_reverse(names)

        return combinations

    def generate_kids_names(self, kids):
        combinations = []
        for kid in kids:
            combinations.append(
                self.generate_names(kid["name"], kid["nickname"]))

        return combinations

    def generate_kids_birthdays(self, kids):
        combinations = []
        for kid in kids:
            combinations.append(
                self.generate_birthdates_combinations(kid["birthdate"]))

        return combinations

    def generate_names(self, name, nickname):
        names = []
        array_names = name.split()
        array_names.append(nickname)

        for aux in array_names:
            names.append(aux)

        names.append(self.combinations_cases(array_names))
        return names

    def generate_birthdates_combinations(self, date):
        combinations = []

        if(not date.isdigit()):
            return combinations
        date = str(date)
        day = date[2:]
        month = date[2:4]
        year = date[4:]
        short_year = year[1:]
        if(int(date[2:]) < 10):
            short_day = day[0:]
        else:
            short_day = day

        if(int(date[2:4]) < 10):
            short_month = str(month[0:])
        else:
            short_month = month

        combinations = [
            date,                                       # normal
            day,                                        # day
            month,                                      # month
            year,                                       # year
            date[::-1],                                 # reverse
            month + day + year,                         # MMDDYYYY
            day + month + short_year,                   # DDMMYY
            month + day + short_year,                   # MMDDYY
            short_day + short_month + short_year,       # DMYY
            short_month + short_day + short_year,       # MDYY
            short_day + short_month + year,             # DMYYYY
            short_month + short_day + year              # MDYYYY
        ]
        return combinations

    def prepare_extra_info(self, info):
        return info.split(",")

    def remove_articles(self, word):
        new_word = ''
        aux = word.split(" ")
        # if(re.match('[a-z\s]*$', name)):
        if(len(aux) == 1):
            return word.title()
        for i in range(0, len(aux)):
            if(not re.match(['\ba\b', '\ban\b', '\bthe\b'], aux[i])):
                if(aux[i].isdigit()):
                    new_word = new_word + str(aux[i])
                else:
                    new_word = new_word + aux[i].title()

        return new_word

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

    @property
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

        work = self.prepare_words(profile["work"])
        city = self.prepare_words(profile["cities"])
        study = self.prepare_words(profile["study"])
        if(profile["extra_info"]):
            extra_info = self.prepare_words(
                self.prepare_extra_info(profile["extra_info"]))
        try:
            likes = self.prepare_words(profile["words"])
        except BaseException:
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
