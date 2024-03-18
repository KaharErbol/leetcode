class Solution:
    def calculate(self, s: str) -> int:
        length = len(s)
        curr_num = 0
        last_num = 0
        res = 0
        op = '+'

        for i in range(length):
            c = s[i]
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            if not c.isdigit() and c != ' ' or i == length - 1:
                if op in ('+', '-'):
                    res += last_num
                    last_num = curr_num if op == '+' else -curr_num
                elif op == '*':
                    last_num *= curr_num
                elif op == '/':
                    last_num = int(last_num / curr_num)
                op = c
                curr_num = 0
        res += last_num
        return res