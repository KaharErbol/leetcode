class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        }

        res = 0 
        prev = 0

        for char in s[::-1]:
            cur = roman[char]
            if cur < prev:
                res -= cur
            else:
                res += cur

            prev = cur
        
        return res