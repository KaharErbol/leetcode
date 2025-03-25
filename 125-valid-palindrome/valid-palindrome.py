class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(s.split())
        for c in s:
            if not c.isalnum():
                s = s.replace(c, '')
        s = s.lower()

        l = 0
        h = len(s) - 1

        while l < h:
            if s[l] != s[h]:
                return False
            l += 1
            h -= 1
        
        return True