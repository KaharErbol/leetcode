class Solution:
    def isHappy(self, n: int) -> bool:
        dic = set()
        while n not in dic:
          dic.add(n)
          n = self.helper(n)
          if n == 1:
            return True
        return False

    def helper(self, n):
      res = 0
      while n:
        d = n % 10
        d = d ** 2
        res += d
        n = n // 10

      return res
          