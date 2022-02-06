# 22'
# this is called First occurence transformation
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.format0(s) == self.format0(t)
    def format0(self, string):
        ret = []
        h = {}
        cur = 0
        for ch in string:
            if h.get(ch) != None:
                ret.append(str(h[ch]))
            else:
                h[ch] = cur
                ret.append(str(cur))
                cur += 1
        return ret

# easier solution
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        cur = head
        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex

        return prev
