class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        cach = set()
        res = 0

        for r in range(len(s)):
            while s[r] in cach:
                cach.remove(s[l])
                l += 1
            cach.add(s[r])
            res = max(res, r - l + 1)
        
        return res