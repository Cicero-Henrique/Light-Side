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
        chars = ['"""', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':',
                    ';', '<', '=', '>', '?', '@', '[', '"\"', ']', '^', '_', '`', '{', '|', '}', '~']
        combinations = []

        # for fword in first_array:
        #     for sword in second_array:
        for char in chars:
            combinations.append(fword + sword + char)
            combinations.append(char + fword + sword)
            combinations.append(fword + char + sword)

            combinations.append(sword + fword + char)
            combinations.append(char + sword + fword)
            combinations.append(sword + char + fword)

        return combinations

    def get_level(self):
        print("Choose the level of combinations: ")
        print("1- Soft")
        print("2- Intermediate")
        print("3- Intense")
        x = 4
        while(int(x) > 3 or int(x) < 1):
            x = input("What you prefer? ")
        return int(x)

    def write_and_replace(self, all_combinations):
        f = open('wordlist.txt', 'w')
        for word in all_combinations:
            f.write(word + '\n')
            f.write(self.replace_by_spec_chars(word) + '\n')
        f.close()

    def write_in_file(self, all_combinations, spechar):
        f = open('wordlist.txt', 'w', encoding='utf8')
        cont = 0
        for word in all_combinations:
            print(str(cont) + "/" + str(len(all_combinations)))
            cont = cont +1
            for word2 in all_combinations:
                combinations = self.generate_words_combinations(word, word2, spechar)

                for combination in combinations:
                    f.write(combination + "\n")
        f.close()

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

    def get_spechar(self):
        answer = input("> Do you want to add special chars at the end of words? Y/[N]: ").lower()
        if(answer == 'y'):
            return True
        else:
            return False

    def __init__(self, profile):

        level = self.get_level()
        spechar = self.get_spechar()
        if(int(level) == 1):
            basewords = self.soft(profile)
        elif (int(level) == 2):
            basewords = self.intermediate(profile)
        else:
            basewords = self.intense(profile)

        basewords = self.remove_duplicates_array(basewords)

        self.write_in_file(basewords, spechar)

