class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        temp = [0 for _ in range(n + 1)]

        for c in citations:
            temp[min(c, n)] += 1

        total = 0
        for i in range(n, -1, -1):
            total += temp[i]
            if total >= i:
                return i
