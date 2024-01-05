class SparseVector:
    # Solution 1
    # def __init__(self, nums: List[int]):
    #     self.arr = nums
    #     self.l = len(nums)

    # Return the dotProduct of two sparse vectors
    # def dotProduct(self, vec: 'SparseVector') -> int:
    #     res = 0
    #     for i in range(self.l):
    #         res += self.arr[i] * vec.arr[i]
    #     return res
        
    # Solution 2
    def __init__(self, nums: List[int]):
        self.arr = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                self.arr[i] = nums[i]

    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for k,v in self.arr.items():
            if k in vec.arr:
                res += v * vec.arr[k]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)