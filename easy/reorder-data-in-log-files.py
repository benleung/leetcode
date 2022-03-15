
'''
40' because troublesome in handling cmparator
'''
class Log:
    def __init__(self, log):
        split_words = log.split()
        self.identifier = split_words[0]
        self.is_letter = 'a' <= split_words[1][0] <= 'z'
        self.contents = " ".join(split_words[1:])

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def cmp(left, right):
            is_left_smaller= False
            
            left = Log(left)
            right = Log(right)
            
            if left.is_letter + right.is_letter == 1: # xor
                is_left_smaller = left.is_letter
            elif left.is_letter and right.is_letter:
                # letter-logs are sorted lexicographically by their contents
                if left.contents != right.contents:
                    is_left_smaller = left.contents < right.contents
                else:
                    is_left_smaller = left.identifier < right.identifier
            else:
                pass # digit-logs maintain their relative ordering
            return -1 if is_left_smaller else 1

        logs.sort(key=cmp_to_key(cmp))
        return logs
