# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        cnt = 0

        h = {}

        if n == 0:
          return head

        while cur:
          cnt += 1
          h[str(cnt)] = cur
          cur = cur.next
          

        print(h)

        rm = cnt - n + 1
        
        if cnt == 1:
          return None
        
        if rm == 1:
          return head.next

        h[str(rm - 1)].next = h[str(rm)].next
        h[str(rm)].next = None

        return head