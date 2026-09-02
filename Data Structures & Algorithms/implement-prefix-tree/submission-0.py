class PrefixTree:

    def __init__(self):
        self.word_end = False
        self.children = {} # map of letter to prefix tree
        

    def insert(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = PrefixTree()
            curr = curr.children[c]
        curr.word_end = True


    def search(self, word: str) -> bool:
        curr = self
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word_end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        