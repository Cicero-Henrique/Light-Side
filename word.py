class Word:

    def generate_word(self, words):
        combinations = []
        combinations += self.combinations_cases(words, "lower")
        combinations += self.combinations_cases(words, "title")
        combinations += self.combinations_reverse(combinations)

        return combinations

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
            combinations.append(word[::-1])

        return combinations

    def __init__(self, array):
        self.word = self.generate_word(array)
