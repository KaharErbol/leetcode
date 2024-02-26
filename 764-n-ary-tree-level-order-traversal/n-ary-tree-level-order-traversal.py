"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        result = []

        def traversal(root, level):
            if len(result) == level:
                result.append([])
            result[level].append(root.val)
            if root.children:
                for i in range(len(root.children)):
                    traversal(root.children[i], level+1)
        
        traversal(root, 0)

        return result