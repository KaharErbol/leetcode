# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        checked = set()
        p = head
        while p:
          if p in checked:
            return True
          checked.add(p)
          p = p.next
        return False