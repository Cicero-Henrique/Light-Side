from word import Word

class WordlistGenerator:

    def combination_words_birthday(self, words, birthdays):
        combinations = []
        for word in words:
            for birthday in birthdays:
                combinations.append(word + birthday)
                combinations.append(birthday + word)
                if(" " in word):
                    aux = word.split()
                    word = ""
                    for i in range(0, len(aux)-1):
                        word = word + aux[i] + birthday
                    combinations.append(word)
        return combinations

    def remove_duplicates_array(self, array):

        duplicates = []
        [duplicates.append(item) for item in array if item not in duplicates]
        return duplicates

    def combine_array(self, arr, spechar):
        combinations = []
        i = 0
        for word1 in arr:
            i = i + 1
            j = 0
            for word2 in arr:
                j = j + 1
                print(str(i) + "/" + str(len(arr)) + "\t\t"+ str(j) + "/" + str(len(arr)))
                combinations = combinations + self.generate_words_combinations(word1, word2, spechar)

        return combinations

    def generate_words_combinations(self, first_word, second_word, spechar):
        combinations = []

        if(spechar):
            combinations.append(first_word + second_word)
            combinations.append(second_word + first_word)
            combinations.append(self.generate_words_combinations_with_special_chars(first_word, second_word))
        else:
            combinations.append(first_word + second_word)
            combinations.append(second_word + first_word)

        return combinations

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

    def soft(self, profile):
        return profile["names"] + profile["birthdays"] + profile["likes"] + profile["city"] + profile["work"] + profile["study"]

    def intermediate(self, profile):

        works = Word(profile["work"]).word
        likes = Word(profile["likes"]).word
        studies = Word(profile["study"]).word
        cities = Word(profile["city"]).word
        return profile["names"] + profile["birthdays"] + likes + cities + works + studies

    def intense(self, profile):
        names_birthdays = self.combination_words_birthday(profile["names"], profile["birthdays"])
        likes_birthdays = self.combination_words_birthday(profile["likes"], profile["birthdays"])
        return self.soft(profile) + names_birthdays + likes_birthdays

    def __init__(self, profile, op, spechar):
        if(op == 1):
            basewords = self.soft(profile)
        elif (op == 2):
            basewords = self.intermediate(profile)
        else:
            basewords = self.intense(profile)

        basewords = self.remove_duplicates_array(basewords)
        combinations = self.combine_array(basewords, spechar)
        self.combinations = combinations



