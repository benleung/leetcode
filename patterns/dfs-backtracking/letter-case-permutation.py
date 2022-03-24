'''
very intuitive if imaginge a tree and want to try all the combinations

7' -> 5' (revisited on march 23)
'''


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        cur = []
        def backtrack(first):
            if len(cur) == len(s):
                ans.append("".join(cur))
                return
            if s[first].isalpha():
                cur.append(s[first].lower())
                backtrack(first+1)
                cur.pop()
                
                cur.append(s[first].upper())
                backtrack(first+1)
                cur.pop()
            else:
                cur.append(s[first])
                backtrack(first+1)
                cur.pop()
        
        backtrack(0)
        return ans
