class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 # It will stop at the elements equal to val

        for i in range(len(nums)): # we check each element on i
            if nums[i] != val: # when it's not val, meaning we will move the curr to k
                nums[k] = nums[i] # because k will stop at elemtns equal to val
                k += 1 # then go to the next one
                # The condition is when the i element != val, 
                # so k will move along when it's not val
        return k
