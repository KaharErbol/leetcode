class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for i in range(len(w)):
            prefix_sum += w[i]
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum
        

    def pickIndex(self) -> int:
        target = random.random() * self.total_sum
        l = 0
        r = len(self.prefix_sums)
        while l < r:
            mid = (l+r) // 2
            if target > self.prefix_sums[mid]:
                l = mid + 1
            else:
                r = mid
        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()