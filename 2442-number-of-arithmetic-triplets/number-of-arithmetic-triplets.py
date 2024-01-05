class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        checked = set()

        for num in nums:
            if num - diff in checked and num - diff * 2 in checked:
                count += 1
            checked.add(num)

        return count
