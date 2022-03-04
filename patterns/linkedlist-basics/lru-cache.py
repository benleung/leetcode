'''
model answer of double linked list
'''

class DLinkedNode(): 
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None
            
class LRUCache():
    def _add_node(self, node):
        """
        Always add the new node right after head.
        """
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """
        Remove an existing node from the linked list.
        """
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        """
        Move certain node in between to the head.
        """
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """
        Pop the current tail.
        """
        res = self.tail.prev
        self._remove_node(res)
        return res

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key, None)
        if not node:
            return -1

        # move the accessed node to the head;
        self._move_to_head(node)

        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self.cache.get(key)

        if not node: 
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node(newNode)

            self.size += 1

            if self.size > self.capacity:
                # pop the tail
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            # update the value.
            node.value = value
            self._move_to_head(node)

'''
linked list solution after looking at hints
'''

class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node() # dummy
        self.last = self.head
        
        self.dict = {}
        self.listPtr = {} # self.listPtr[key] is the key's node
    
    def moveToEnd(self, key):
        if self.last.val ==key:
            # already at the end
            return
        
        if key in self.listPtr:
            # remove from existing list
            self.deleteNode(key)
        nodeToAdd = Node(key)
        self.listPtr[key] = nodeToAdd
            
        # add to end of list
        self.last.next = nodeToAdd
        nodeToAdd.next = None
        nodeToAdd.prev = self.last
        
        self.last = nodeToAdd

    def deleteNode(self, key):
        targetNode = self.listPtr[key]
        del self.listPtr[key]
        targetNode.prev.next = targetNode.next
        if targetNode.next:
            targetNode.next.prev = targetNode.prev

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        self.moveToEnd(key)
        return self.dict[key]

    def put(self, key: int, value: int) -> None:
        self.moveToEnd(key)
        self.dict[key] = value
        print(key)
        if len(self.dict) > self.capacity:
            lruKey = self.head.next.val
            del self.dict[lruKey]
            self.deleteNode(lruKey)
            
        self.dict[key] = value

'''
didn't have knowledge in OrderDict so unable to solve this problem
'''

from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.orderDict = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.orderDict:
            return -1
        self.orderDict.move_to_end(key)
        return self.orderDict[key]

    def put(self, key: int, value: int) -> None:
        if key in self.orderDict:
            self.orderDict.move_to_end(key)
        elif len(self.orderDict) == self.capacity:
            self.orderDict.popitem(last = False)
        self.orderDict[key] = value
