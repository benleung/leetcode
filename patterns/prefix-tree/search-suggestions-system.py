'''
revisited on 2/26
should revisit again
about 30'
'''

class Trie:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word):
        node  = self.root
        for c in word:
            if c not in node.next:
                node.next[c] = TreeNode()
                node = node.next[c]
                '''
                this is different from
                node = node.next[c] = TreeNode()
                '''
            else:
                node = node.next[c]
            node.words.append("".join(word))
            
    def getWordsWithPrefix(self, prefix):
         # maximum count of 3
        node  = self.root
        for i, c in enumerate(prefix):
            if c not in node.next:
                return []
            else:
                node = node.next[c]
            if i == len(prefix)-1:
                node.words.sort()
                return node.words[:3]
        
class TreeNode:
    def __init__(self):
        self.next = {} # "character" -> TreeNode
        self.words = list()

class Solution:
    def suggestedProducts(self, A: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for a in A:
            trie.insert(a)
        
        ans = []
        word = ""
        for c in searchWord:
            word += c
            row = trie.getWordsWithPrefix(word)
            ans.append(row)
        
        return ans

# example of without using trie https://leetcode.com/problems/search-suggestions-system/discuss/436564/Python-A-simple-approach-without-using-Trie

# best explaination
# https://leetcode.com/problems/search-suggestions-system/discuss/864637/Python-3-or-Two-Methods-(Sort-Trie)-or-Explanation

'''
copied from solution

techniques:
- root is dummy (val/words doesn't matter for root, children matters)
- children is in type of dict
'''
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.words = list()
        self.n = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children: node.children[c] = TrieNode()
            node = node.children[c] 
            if node.n < 3:
                node.words.append(word)
                node.n += 1
        
    def find_word_by_prefix(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children: return ''
            node = node.children[c] 
        return node.words
            
class Solution:
    def suggestedProducts(self, A: List[str], searchWord: str) -> List[List[str]]:
        A.sort()
        trie = Trie()
        for word in A: trie.add_word(word)
        ans, cur = [], ''
        for c in searchWord:
            cur += c 
            ans.append(trie.find_word_by_prefix(cur))
        return ans   
