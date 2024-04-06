class Solution:
    def binaryExpo(self, x: float, n: int) -> float: 
        if n == 0:
            return 1
        
        if n < 0:
            return 1.0 / self.binaryExpo(x, -1 * n)

        if n % 2 == 1:
            return x * self.binaryExpo(x * x, (n-1) // 2)
        else:
            return self.binaryExpo(x * x, n //2)

    def myPow(self, x: float, n: int) -> float:
        return self.binaryExpo(x, n)
