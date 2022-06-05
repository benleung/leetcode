'''
28'
'''
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        ans = 0
        count_start_with = {}
        h = defaultdict(list)
        
        for word in words:
            h[len(word)].append(word)
        
        def is_valid_next_word(word, next_word):
            slow = 0
            if slow == len(word):
                return True
            for fast in range(0, len(next_word)):
                if next_word[fast] == word[slow]:
                    slow += 1
                if fast-slow >1:
                    return False
                if slow == len(word):
                    return True
                    
            return False
        
        # count the chain that starts with word
        def dfs(word):
            N = len(word)

            if word in count_start_with:
                return count_start_with[word]
            
            if h[N+1] == []:
                count_start_with[word] = 1
                return 1

            count = 1
            for next_word in h[N+1]:
                if is_valid_next_word(word, next_word):
                    count = max(count, dfs(next_word)+1)
            count_start_with[word] = count
            return count
        
        for word in words:
            ans = max(ans, dfs(word))
        
        return ans
