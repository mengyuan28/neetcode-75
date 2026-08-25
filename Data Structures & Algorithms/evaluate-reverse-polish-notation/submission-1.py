class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if not tokens:
            return 0
        for i in range(0, len(tokens)):
            cur_token = tokens[i]
            if cur_token not in "+-*/":
                stack.append(int(cur_token))
            else:
                if len(stack) < 2:
                    break
                last = stack.pop()
                second = stack.pop()
                if cur_token == "+":
                    num = int(last) + int(second)
                    stack.append(num)
                elif cur_token == "-":
                    num = int(second) - int(last)
                    stack.append(num)
                elif cur_token == "*":
                    num = int(second) * int(last)
                    stack.append(num)
                elif cur_token == "/":
                    if int(last) == 0:
                        break
                    num = int(float(second) / last)
                    stack.append(num)
        return stack[0]
