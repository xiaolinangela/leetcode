class WordDictionary:

    def __init__(self):
        self.d = defaultdict(set)

    def add_word(self, word):
        self.[(len(word))].add(word)

    def search(word):
        m = len(word):
        for dict_word in self.d[m]:
            i = 0
            while i < m and (dict_word[i] == word[i] or dict_word[i] == "."):
                i += 1
            if i == m:
                return True
        return False
