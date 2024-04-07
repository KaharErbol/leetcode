class Solution:
    def binaryExpo(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.binaryExpo(x, -n)

        if n % 2 == 0:
            return self.binaryExpo(x * x, n // 2)
        
        if n % 2 != 0:
            return x * self.binaryExpo(x * x, (n-1) // 2)

    def myPow(self, x: float, n: int) -> float:
        return self.binaryExpo(x, n)
        
       
                

