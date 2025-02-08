class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Kahar
        def helper(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        k = k % len(nums)
        # Revers the whole array
        helper(0, len(nums) - 1)

        # Revers the left side
        helper(0, k - 1)

        # Reverse the right side
        helper(k, len(nums) - 1)