class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        left = 0
        right = n
        while left < n:
            result.append(nums[left])
            result.append(nums[right])
            left += 1
            right += 1
        return result