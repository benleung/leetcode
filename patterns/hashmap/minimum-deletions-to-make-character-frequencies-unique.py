'''
15'
there's is better solution by sorting
'''
class Solution:
    def minDeletions(self, s: str) -> int:
        ch_to_freq = Counter(s)
        freqs = set()
        ans = 0
        
        def find_available_freq(freq):
            for i in range(freq, -1, -1):
                if i not in freqs:
                    return i
            return 0
        
        for freq in ch_to_freq.values():
            available_freq = find_available_freq(freq)
            if available_freq!= 0:
                freqs.add(available_freq)
            ans += freq - available_freq
        
        return ans
