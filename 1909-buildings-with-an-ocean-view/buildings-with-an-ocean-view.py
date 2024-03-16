class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        tallest = -1
        for i in range(len(heights)-1,-1,-1):
            if heights[i] > tallest:
                tallest = heights[i] 
                res.append(i)
        return sorted(res)