class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        return [
            candidate for candidate in word_list
            if candidate.lower() != self.word and
               sorted(candidate.lower()) == sorted(self.word)
        ]

