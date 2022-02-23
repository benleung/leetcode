

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
