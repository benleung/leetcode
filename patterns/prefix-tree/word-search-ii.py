'''
written by myself
at least 30'
passing node in backtracking
'''
class Node:
    def __init__(self):
        self.next = {}
        self.word = None

class Trie:
    
    def __init__(self):
        self.root = Node()
        
    def add(self, word):
        cur = self.root
        for i,c in enumerate(word):
            if c not in cur.next:
                cur.next[c] = Node()
            cur  = cur.next[c]
            
            if i == len(word)-1:
                cur.word = word
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        ans = set()
        M = len(board)
        N = len(board[0])
        
        
        for word in words:
            trie.add(word)
        
        self.candidate = []

        def backtrack(row, col, parent):
            letter = board[row][col]
            
            if letter not in parent.next:
                return
            currNode = parent.next[letter]
            
            word_match = currNode.word
            if word_match:
                ans.add(word_match)
            
            board[row][col] = "#" 
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset     
                if newRow < 0 or newRow >= M or newCol < 0 or newCol >= N:
                    continue
                backtrack(newRow, newCol, currNode)
            
            board[row][col] = letter
        
        for m in range(M):
            for n in range(N):
                backtrack(m,n, trie.root)
        
        return list(ans)

'''
copied from solution
'''
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'
        
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word
        
        rowNum = len(board)
        colNum = len(board[0])
        
        matchedWords = []
        
        def backtracking(row, col, parent):    
            
            letter = board[row][col]
            currNode = parent[letter]
            
            # check if we find a match of word
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                #   as well as avoiding using set() for results.
                matchedWords.append(word_match)
            
            # Before the EXPLORATION, mark the cell as visited 
            board[row][col] = '#'
            
            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset     
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)
        
            # End of EXPLORATION, we restore the cell
            board[row][col] = letter
        
            # Optimization: incrementally remove the matched leaf node in Trie.
            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)
        
        return matchedWords    
