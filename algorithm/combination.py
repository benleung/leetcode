from itertools import combinations

# print(set(combinations([1, 2, 3, 4], 2)))

def n_length_combo(lst, n):
     
    if n == 0:
        return [[]]
     
    l =[]
    for i in range(0, len(lst)):
         
        m = lst[i]
        remLst = lst[i + 1:]
         
        for p in n_length_combo(remLst, n-1):
            l.append([m]+p)
             
    return l
 
# Driver code
# if __name__=="__main__":
#     arr ="abc"
#     print(n_length_combo([x for x in arr], 2))

print(n_length_combo([1,2,3,4], 2))
