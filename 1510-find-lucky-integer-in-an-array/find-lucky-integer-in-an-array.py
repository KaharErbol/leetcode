class Solution:
    def findLucky(self, arr: List[int]) -> int:
        frequency = {}
        res = -1
        for i in range(len(arr)):
            if arr[i] not in frequency:
                frequency[arr[i]] = 0
            frequency[arr[i]] += 1
        for k,v in frequency.items():
            if k == v:
                res = max(res, k)
        return res 