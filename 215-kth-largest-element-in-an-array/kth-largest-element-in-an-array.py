class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(nums, k):
            p = random.choice(nums)
            l, m, r = [], [], []

            for num in  nums:
                if num > p:
                    l.append(num)
                elif num < p:
                    r.append(num)
                else:
                    m.append(num)

            if k <= len(l):
                return quick_select(l, k)
            if k > len(l) + len(m):
                return quick_select(r, k - len(l) - len(m))
            return p
        return quick_select(nums, k)