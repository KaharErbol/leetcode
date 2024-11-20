class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        ps = 0
        d = { 0:1 }
        for num in nums:
            ps += num
            if ps - k in d:
                res += d[ps - k]
            if ps not in d:
                d[ps] = 0
            d[ps] += 1
        
        return res