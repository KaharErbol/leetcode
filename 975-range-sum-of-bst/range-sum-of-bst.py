# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.checked = set()

    def checkVal(self, val, low, high):
            if val >= low and val <= high:    
                return val
            else:
                return 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        _sum = 0
        curr = root
        if curr:
            if curr not in self.checked:
                _sum += self.checkVal(curr.val, low, high)
                self.checked.add(curr)
            if curr.left:
                _sum += self.checkVal(curr.left.val, low, high)
                self.checked.add(curr.left)
            if curr.right:
                _sum += self.checkVal(curr.right.val, low, high)
                self.checked.add(curr.right)
                
            _sum += self.rangeSumBST(curr.left, low, high)
            _sum += self.rangeSumBST(curr.right, low, high)

        return _sum    
            