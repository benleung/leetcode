# https://leetcode.com/problems/design-a-number-container-system/

# 2 hashmap
'''
forget iterating when for looping
n2i, i2n are good naming conventions
learn about SortedList
should do again
'''

# Sorted List
from sortedcontainers import SortedList
class NumberContainers:    
    def __init__(self):
        self.i2n = {}
        self.n2i = defaultdict(SortedList)

    def change(self, index: int, number: int) -> None:
        if index in self.i2n:
            oldnumber = self.i2n[index]
            self.n2i[oldnumber].discard(index)
        self.n2i[number].add(index)
        self.i2n[index] = number
        

    def find(self, number: int) -> int:
        if len(self.n2i[number]) > 0:
            return self.n2i[number][0]
        else:
            return -1

# TLE
class NumberContainers:    
    def __init__(self):
        self.index_to_num = {}
        self.num_index_tuples = [] # (number, index)
        

    def change(self, index: int, number: int) -> None:
        
        if index not in self.index_to_num:
            self.index_to_num[index] = number
            i = len(self.num_index_tuples)
            self.num_index_tuples.append((number, index))
            while i-1 >= 0 and self.num_index_tuples[i] <= self.num_index_tuples[i-1]:
                self.num_index_tuples[i], self.num_index_tuples[i-1] = self.num_index_tuples[i-1], self.num_index_tuples[i]
                i -= 1
        else:
            original_num = self.index_to_num[index]
            i = bisect_left(self.num_index_tuples, (original_num, index))
            if i < len(self.num_index_tuples) and self.num_index_tuples[i] == (original_num, index):
                self.num_index_tuples[i] = (number, index)
            
            # move left
            while i-1 >= 0 and self.num_index_tuples[i] < self.num_index_tuples[i-1]:
                self.num_index_tuples[i], self.num_index_tuples[i-1] = self.num_index_tuples[i-1], self.num_index_tuples[i]
                i -= 1
            
            # move right
            while i+1 < len(self.num_index_tuples) and self.num_index_tuples[i] > self.num_index_tuples[i+1]:
                self.num_index_tuples[i], self.num_index_tuples[i+1] = self.num_index_tuples[i+1], self.num_index_tuples[i]
                i += 1
            
            self.index_to_num[index] = number
            

    def find(self, number: int) -> int:
        # smallest index
        i = bisect_left(self.num_index_tuples, (number, 0))
        # print(self.num_index_tuples)
        if i < len(self.num_index_tuples) and self.num_index_tuples[i][0] == number:
            return self.num_index_tuples[i][1]
        else:
            return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
