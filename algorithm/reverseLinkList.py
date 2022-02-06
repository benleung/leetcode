def reverseList(self, head):
  prev = None
  cur = head

  while cur:
    nex = cur.next
    cur.next = prev
    prev = cur
    cur = next
  return prev
