# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()
        tail = newHead
        carry = 0

        while l1 or l2 or carry != 0:
          d1 = l1.val if l1 else 0
          d2 = l2.val if l2 else 0

          s = d1 + d2 + carry
          digit = s % 10
          carry = s // 10

          newNode = ListNode(digit)
          tail.next = newNode
          tail = tail.next

          l1 = l1.next if l1 else None
          l2 = l2.next if l2 else None
        
        return newHead.next

