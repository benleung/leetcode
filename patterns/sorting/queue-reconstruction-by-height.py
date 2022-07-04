'''
have a neater way to solve this
'''
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        N = len(people)
        ans = [None]*N
        people.sort()

        height = None
        i = 0
        heigher_people = 0
        for person in people:
            if person[0] != height:
                height = person[0]
                heigher_people = 0  
                i = 0
            
            if person == [7,1]:
                pass
            
            while i < N:
                if ans[i] == None: # potential for higher height found
                    if heigher_people == person[1]:
                        ans[i] = person
                        heigher_people += 1
                        break
                    heigher_people += 1
                i += 1
        
        return ans
