# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leftPrev = dummy
        cur = head

        # Place cur on left, and leftPrev before it
        for i in range(left - 1):
          leftPrev = cur
          cur = cur.next

        # Reverse Nodes between left and right
        prev = None
        for i in range(right - left + 1):
          temp = cur.next
          cur.next = prev
          prev = cur
          cur = temp

        # Connect the left adn right tails to the correct nodes
        leftPrev.next.next = cur
        leftPrev.next = prev

        return dummy.next



