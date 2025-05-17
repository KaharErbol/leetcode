# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
          return head
        
        last_node = head
        cnt = 1

        while last_node.next:
          last_node = last_node.next
          cnt += 1

        k = k % cnt

        last_node.next = head

        temp = head

        for _ in range(cnt - k - 1):
          temp = temp.next

        result = temp.next
        temp.next = None

        return result

        