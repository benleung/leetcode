'''
15'
careless:
- cur.next instead cur (dun forget)
'''
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = {}

class FileSystem(object):

    def __init__(self):
        self.root = Node()

    def createPath(self, path, value):
        """
        :type path: str
        :type value: int
        :rtype: bool
        """
        
        cur  = self.root
        folders = path.split("/")
        if len(folders)<=1:
            return False
        for i in range(1,len(folders)):
            folder = folders[i]
            if i == len(folders)-1:
                if folder in cur.next:
                    # path already exists
                    return False
                else:
                    cur.next[folder] = Node(value)
                    return True
            else:
                if folder in cur.next:
                    cur = cur.next[folder]
                else:
                    # parent path doesn't exist
                    return False

    def get(self, path):
        """
        :type path: str
        :rtype: int
        """
        folders = path.split("/")
        if len(folders)<=1:
            return -1
        cur = self.root
        for i in range(1,len(folders)):
            folder = folders[i]
            if folder in cur.next:
                cur = cur.next[folder]
            else:
                # parent path doesn't exist
                return -1
        return cur.val
