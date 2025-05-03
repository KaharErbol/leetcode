class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""

        for c in path + "/": # The "/" at the end helps with the case path doesn't have one
          if c == "/":
            if cur == "..": 
              if stack:
                stack.pop()
            elif cur != "." and cur != "":
              stack.append(cur)
            cur = ""
          else:
            cur += c
        
        return "/" + "/".join(stack)