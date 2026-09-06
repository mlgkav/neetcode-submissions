class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
        

    def search(self, word: str) -> bool:
        def dfs(root, i):
            if i == len(word):
                return root.word

            c = word[i]
            if c == ".":
                for child in root.children.values():
                    if dfs(child, i + 1):
                        return True
                return False

            return c in root.children and dfs(root.children[c], i + 1)

        return dfs(self.root, 0)