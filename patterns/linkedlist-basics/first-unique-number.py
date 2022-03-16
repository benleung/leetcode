'''
15'
'''
class Node:
    def __init__(self, val=None):    
        self.prev = None
        self.next = None
        self.val = val

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.duplicate_set = set()
        self.nodes = {} # val -> node
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        if self.head.next.val:
            return self.head.next.val
        else:
            return -1

    def add(self, value: int) -> None:
        if value in self.duplicate_set:
            return
        if value in self.nodes:
            self.remove(self.nodes[value])
        else:
            tail_prev = self.tail.prev
            new_node = Node(value)
            
            tail_prev.next = new_node
            self.tail.prev = new_node
            new_node.prev = tail_prev
            new_node.next = self.tail
            
            self.nodes[value] = new_node
            
    def remove(self, node):
        prev_tmp, next_tmp = node.prev, node.next
        prev_tmp.next = next_tmp
        next_tmp.prev = prev_tmp
        self.duplicate_set.add(node.val)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
