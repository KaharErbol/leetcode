class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        i = 0
        while i < len(nums):
          n = nums[i]
          print(f"Current n: {n}")
          if n - 1 not in nums:
            length = 0
            while n + length in nums:
              print(f"Iteration lenth: {length}")
              length += 1
            print(f"Final length: {length}")
            if n == n+length-1:
              result.append(f"{n}")
            else:  
              result.append(f"{n}->{n+length-1}")
          i = i + length
          print(f"next i: {i}")
        return result