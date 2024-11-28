class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(base=x, exp=abs(n)):
            if exp == 0:
                return 1
            elif exp % 2 == 1:
                return base * helper(base*base, (exp-1) // 2)
            else:
                return helper(base*base, exp // 2)

        res = helper()
    
        return float(res) if n > 0 else 1 / res