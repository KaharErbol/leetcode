class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        tallest = -1
        for i in range(len(heights)-1,-1,-1):
            if heights[i] > tallest:
                tallest = heights[i] 
                res.append(i)
        res.sort()
        return res

        # stack = []
        
        # for i in range(len(heights)):
        #     while stack and heights[stack[-1]] <= heights[i]:
        #         stack.pop()
        #     stack.append(i)
        # return stack
