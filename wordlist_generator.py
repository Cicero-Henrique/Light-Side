from word import Word
import view
import time


class WordlistGenerator(Word):

    def combination_words_birthday(self, words, birthdays):
        combinations = []
        for word in words:
            for birthday in birthdays:
                combinations.append(word + birthday)
                combinations.append(birthday + word)
                if(" " in word):
                    aux = word.split()
                    word = ""
                    for i in range(0, len(aux) - 1):
                        word = word + aux[i] + birthday
                    combinations.append(word)
        return combinations

    def remove_duplicates_array(self, array):

        duplicates = []
        [duplicates.append(item) for item in array if item not in duplicates]
        return duplicates

    def generate_words_combinations(self, first_word, second_word, spechar):
        combinations = []

        if(spechar):
            combinations.append(first_word + second_word)
            combinations.append(second_word + first_word)
            combinations += self.generate_words_combinations_with_special_chars(first_word, second_word)
        else:
            combinations.append(first_word + second_word)
            combinations.append(second_word + first_word)

        combinations = self.remove_duplicates_array(combinations)
        return combinations

    def generate_words_combinations_with_special_chars(self, fword, sword):
        chars = ['"""', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*',
                 '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@',
                 '[', '"\"', ']', '^', '_', '`', '{', '|', '}', '~']
        combinations = []

        for char in chars:
            combinations.append(fword + sword + char)
            combinations.append(char + fword + sword)
            combinations.append(fword + char + sword)

            combinations.append(sword + fword + char)
            combinations.append(char + sword + fword)
            combinations.append(sword + char + fword)

        return combinations

    def get_level(self):
        view.clear()
        print("Choose the level of combinations: ")
        print("1- Soft")
        print("2- Intermediate")
        print("3- Intense")
        x = 4
        while(x != '1' and x != '2' and x != '3'):
            x = input("What you prefer? ")
        return x

    def write_in_file(self, all_combinations, spechar, info, profile):
        f = open('wordlist.txt', 'w', encoding='utf8')
        cont = 0
        view.clear()
        view.show_info(profile)
        for word in all_combinations:
            view.percentage(int(cont), int(len(all_combinations)))
            cont = cont + 1
            for word2 in all_combinations:
                combinations = self.generate_words_combinations(
                    word, word2, spechar)

                for combination in combinations:
                    if(len(combination) > 8 and len(combination) < 30):
                        f.write(combination + "\n")
        view.percentage(int(len(all_combinations)), int(len(all_combinations)))
        f.close()

    def soft(self, profile):
        return profile["names"] + profile["birthdays"] + profile["likes"] + \
            profile["city"] + profile["work"] + profile["study"]

    def intermediate(self, profile):
        works = self.generate_word(profile["work"])
        likes = self.generate_word(profile["likes"])
        studies = self.generate_word(profile["study"])
        cities = self.generate_word(profile["city"])
        return profile["names"] + profile["birthdays"] + \
            likes + cities + works + studies

    def intense(self, profile):
        names_birthdays = self.combination_words_birthday(
            profile["names"], profile["birthdays"])
        likes_birthdays = self.combination_words_birthday(
            profile["likes"], profile["birthdays"])
        return self.soft(profile) + names_birthdays + likes_birthdays

    def get_spechar(self):
        answer = input(
            "> Do you want to add special chars at the end of words? Y/[N]: ").lower()
        if(answer == 'y'):
            return True
        else:
            return False

    def stopWatch(self, value):
        '''From seconds to days;hours:minutes;seconds'''

        valueD = (((value / 365) / 24) / 60)
        days = int(valueD)

        valueH = (valueD - days) * 365
        hours = int(valueH)

        valueM = (valueH - hours) * 24
        minutes = int(valueM)

        valueS = (valueM - minutes) * 60
        seconds = int(valueS)

        print(days, ";", hours, ":", minutes, ";", seconds)

    def __init__(self, info, profile):

        level = self.get_level()
        spechar = self.get_spechar()
        if(int(level) == 1):
            basewords = self.soft(info)
        elif (int(level) == 2):
            basewords = self.intermediate(info)
        else:
            basewords = self.intense(info)

        basewords = self.remove_duplicates_array(basewords)
        start = time.time()
        self.write_in_file(basewords, spechar, info, profile)
        end = time.time()
        self.stopWatch(end - start)
