class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l = 0
        h = len(s) - 1

        while l < h:
            if not s[l].isalnum():
                l += 1
            elif not s[h].isalnum():
                h -= 1
            else:
                if s[l].lower() != s[h].lower():
                    return False
                else:
                    l += 1
                    h -= 1
        
        return True

            
        
        return True