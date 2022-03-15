'''
7'
'''

class Node:
    def __init__(self):
        self.words = set()
        self.nex = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for i, c in enumerate(word):
            if c not in cur.nex:
                cur.nex[c] = Node()
            cur = cur.nex[c]
            cur.words.add(word)
            if i == len(word)-1:
                cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        for i, c in enumerate(word):
            if c not in cur.nex:
                return False
            cur = cur.nex[c]
            if i == len(word)-1:
                return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i, c in enumerate(prefix):
            if c not in cur.nex:
                return False
            cur = cur.nex[c]
        else:
            return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
