from abc import ABC, abstractmethod


class Word(ABC):

    def get_lower(self, words):
        combinations = []
        for word in words:
            combinations.append(str(word.lower()))
        return combinations

    def get_upper(self, words):
        combinations = []
        for word in words:
            combinations.append(str(word.upper()))
        return combinations

    def get_title(self, words):
        combinations = []
        for word in words:
            combinations.append(str(word.title()))
        return combinations

    def get_camel(self, words):
        combinations = []
        for word in words:
            combinations.append(str(word.lower()))

        for i in range(0, len(words)):
            for j in range(0, len(words)):
                combinations.append(words[i] + words[j].title())
        return combinations

    def get_reverse(self, words):
        combinations = []
        for word in words:
            combinations.append(word[::-1])

        return combinations

    def generate_word(self, words):
        combinations = []
        combinations += self.get_lower(words)
        combinations += self.get_title(words)
        combinations += self.get_reverse(combinations)

        return combinations

    def __init__(self, array):
        super().__init__()
