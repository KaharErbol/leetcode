class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for each in tokens:
          if each == '+':
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1 + num2)
          elif each == '-':
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1 - num2)
          elif each == '*':
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1 * num2)
          elif each == "/":
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(int(num1 / num2))
          else:
            stack.append(int(each))
          
        return stack[0]