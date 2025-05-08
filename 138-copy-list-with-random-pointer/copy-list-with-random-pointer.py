"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_map = {None: None}

        p = head

        while p:
          copy = Node(p.val)
          hash_map[p] = copy
          p = p.next

        p = head

        while p:
          copy = hash_map[p]
          copy.next = hash_map[p.next]
          copy.random = hash_map[p.random]
          p = p.next

        return hash_map[head]