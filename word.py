from abc import ABC, abstractmethod


class Word(ABC):

    def _map(self, words, mapper):
        return [mapper(word) for word in words]

    def _map_builtin_str(self, words, function_name):
        return self._map(words, lambda w: getattr(w, function_name)())

    def get_lower(self, words):
        return self._map_builtin_str(words, 'lower')

    def get_upper(self, words):
        return self._map_builtin_str(words, 'upper')

    def get_title(self, words):
        return self._map_builtin_str(words, 'title')

    def get_camel(self, words):
        combinations = self.get_lower(words)

        for i in range(0, len(words)):
            for j in range(0, len(words)):
                combinations.append(words[i] + words[j].title())
        return combinations

    def get_reverse(self, words):
        return self._map(words, lambda w: w[::-1])

    def generate_word(self, words):
        combinations = self.get_lower(words) + self.get_title(words)
        return combinations + self.get_reverse(combinations)

    def __init__(self):
        super().__init__()
