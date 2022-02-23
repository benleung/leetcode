from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dic = Counter(chars)
        count = 0
        
        for word in words:
            w = Counter(word)
            for key,value in w.items():
                if value>dic[key]:
                    break
            else:
                count += len(word)
        return count
