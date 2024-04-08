class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for point in points:
            print(point)
            dist = point[0] ** 2 + point[1] ** 2
            heapq.heappush(min_heap, (dist, point))

        res = []

        while k > 0:
            res.append(heapq.heappop(min_heap)[1])
            k -= 1
        return res
        


