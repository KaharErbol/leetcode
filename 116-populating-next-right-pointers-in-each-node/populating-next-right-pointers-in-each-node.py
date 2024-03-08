"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # BFS Solution
        # q = []
        # q.append(root)

        # if root == None:
        #     return None

        # while q:
        #     size = len(q)
        #     while size > 0:
        #         node = q.pop(0)
        #         size -= 1
        #         if size > 0:
        #             node.next = q[0]
                
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        # return root

        # DFS Solution
        self.dfs(root)
        return root
    
    def dfs(self, root):
        if root == None or root.left == None:
            return
        root.left.next = root.right
        if root.next != None:
            root.right.next = root.next.left
        self.dfs(root.left)
        self.dfs(root.right)
            
        