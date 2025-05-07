class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
          '+': lambda a, b: a + b,
          '-': lambda a, b: a - b,
          '*': lambda a, b: a * b,
          '/': lambda a, b: a / b
        }
        stack = []
        for each in tokens:
          if each in operators:
            num2 = stack.pop()
            num1 = stack.pop()
            print(f"OP: {each}")
            print(f"num1: {num1} ----- num2: {num2}")
            result = operators[each](num1, num2)
            print(f"After op result: {result}")
            stack.append(int(result))
          else:
            stack.append(int(each))
        
        return stack.pop()