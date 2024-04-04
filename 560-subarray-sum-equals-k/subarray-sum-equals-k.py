class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        hash_map = {0:1}
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in hash_map:
                count += hash_map[prefix_sum - k]
            hash_map[prefix_sum] = 1 + hash_map.get(prefix_sum, 0)
        return count