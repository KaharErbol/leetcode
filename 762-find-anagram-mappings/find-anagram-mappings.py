class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = [None] * len(nums1)

        for i in range(len(nums1)):
            idx = nums2.index(nums1[i])
            mapping[i] = idx
        
        return mapping