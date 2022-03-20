'''
16' TLV
'''
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        
        '''
        ["Hello","World"] -> 5#Hello5#World
        '''
        ans = []
        for s in strs:
            ans.append("{0}#{1}".format(len(s), s))
        return "".join(ans)

    
    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        i=0
        ans = []
        
        def fetch_cur_length(i): # (cur_length, new_i) # new_i is the start index of a word
            cur_length_str = ""
            while s[i] != "#":
                cur_length_str += s[i]
                i += 1
            else:
                return (int(cur_length_str), i+1)
        
        while i < len(s):
            cur_length, new_i = fetch_cur_length(i)
            ans.append(s[new_i:new_i+cur_length])
            
            i = new_i + cur_length
            
        return ans
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
