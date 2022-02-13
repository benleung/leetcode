'''
1 hr but not able to think out of the solution
good thought on coming up the formula of  len(word1)+len(word2)-2*(len(lcs))-replacableCount
however, wrong thought that all combinations of lcs can be obtained easily

learn
- algorithm to obtain an lcs sequence ( instead of the number)
- algorithm to obtain come up with replacableCount regardless of lcs
'''


'''
this problem is a Levenshtein distance problem, but it's not worthwhile to study because too hard(memory check only), and not probably to be asked during an interview
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        # Function to find lcs_algo
        def lcs_algo(S1, S2):
            m = len(S1)
            n = len(S2)
            L = [[0 for x in range(n+1)] for x in range(m+1)]

            # Building the mtrix in bottom-up way
            for i in range(m+1):
                for j in range(n+1):
                    if i == 0 or j == 0:
                        L[i][j] = 0
                    elif S1[i-1] == S2[j-1]:
                        L[i][j] = L[i-1][j-1] + 1
                    else:
                        L[i][j] = max(L[i-1][j], L[i][j-1])

            # find out the sequence
            index = L[m][n]

            lcs_algo = [""] * (index+1)
            lcs_algo[index] = ""

            i = m
            j = n
            while i > 0 and j > 0:

                if S1[i-1] == S2[j-1]:
                    lcs_algo[index-1] = S1[i-1]
                    i -= 1
                    j -= 1
                    index -= 1

                elif L[i][j-1] == L[i][j]:
                    j -= 1 #follow the bigger value (same as current value) in the table   # L[i-1][j] == L[i][j] might be easier to understand,  will lead to the index that S1[i-1] == S2[j-1]
                else:
                    i -= 1

            # Printing the sub sequences
            return "".join(lcs_algo)
            
        lcs = lcs_algo(S1, S2)
        
        p1, p2, p = 0, 0, 0
        replacableCount = 0
        while p < len(lcs) and p1 < len(word1) and p2 < len(word2):
            if word1[p1]  != lcs[p] and word2[p2]  != lcs[p]:
                p1 += 1
                p2 += 1
                replacableCount += 1
            elif word1[p1]  == lcs[p] and word2[p2]  == lcs[p]:
                p1 += 1
                p2 += 1
                p +=1
            elif word1[p1]  != lcs[p]:
                p1 += 1
            else:
                p2 += 1
                
        return len(word1)+len(word2)-2*(len(lcs))-replacableCount
        
        