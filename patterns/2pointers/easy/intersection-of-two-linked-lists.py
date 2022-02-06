# 20'
# point: forcibly convert link list to list

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        listA = []
        listB = []
        rootA = headA
        rootB = headB
        
        while rootA is not None:
            listA.append(rootA)
            rootA = rootA.next
        while rootB is not None:
            listB.append(rootB)
            rootB = rootB.next
        listA.reverse()
        listB.reverse()
        for i in xrange(0, min(len(listA), len(listB))):
            if listA[i] != listB[i]:
                return listA[i-1] if i>0 else None
        return listA[min(len(listA), len(listB))-1]

# a better solution is to use a hash table instead
