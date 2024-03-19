# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = []
        q.append((0, root))

        d = {}
        res =[]

        min_x = float('inf')
        max_x = float('-inf')

        while q:
            x,node = q.pop(0)
            
            if not x in d:
                d[x] = [node.val]
            else:
                d[x].append(node.val)

            min_x = min(min_x, x)
            max_x = max(max_x, x)

            if node.left: q.append((x-1, node.left))
            if node.right: q.append((x+1, node.right))
        
        for i in range(min_x, max_x+1):
            res.append(d[i])
        
        return res
