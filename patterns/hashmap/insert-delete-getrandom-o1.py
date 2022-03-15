'''
not diffciult but not smart enough
12' after knowing sol
bad
- many careless mistakes
'''
class RandomizedSet:

    def __init__(self):
        self.h = {} # val -> index
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.h:
            return False
        else:
            self.array.append(val)
            self.h[val] = len(self.array)-1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.h:
            return False
        
        index = self.h[val]
        del self.h[val]
        
        popped_item = self.array.pop()
        if index < len(self.array): # a different value is popped
            self.array[index] = popped_item
            self.h[popped_item] = index
        
        return True

    def getRandom(self) -> int:
        return self.array[ random.randrange(len(self.array)) ]
