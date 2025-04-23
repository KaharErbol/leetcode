class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
          return False
        
        map_s = {}

        for char in s:
          if char not in map_s:
            map_s[char] = 0
          map_s[char] += 1
        
        print(f"map_s: {map_s}")

        for char in t:
          if char not in map_s or map_s[char] == 0: 
            return False
          map_s[char] -= 1
        
        return True
          
