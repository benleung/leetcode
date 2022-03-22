'''
without bug
'''

class Node:
    def __init__(self):
        self.next = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for i, ch in enumerate(word):
            if ch not in cur.next:
                cur.next[ch] = Node()
            cur = cur.next[ch]
            if i == len(word)-1:
                cur.is_end = True

    def search(self, word: str) -> bool:
        
        def dfs(node, i):
            if i == len(word):
                return node.is_end
            ch = word[i]
            if ch != '.':
                if ch in node.next:
                    return dfs(node.next[ch], i+1)
                else:
                    return False
            else:
                for key in node.next:
                    if dfs(node.next[key], i+1):
                        return True
                return False
        
        return dfs(self.root, 0)
