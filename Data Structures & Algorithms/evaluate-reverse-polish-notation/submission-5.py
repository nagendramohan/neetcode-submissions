class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # res = 0
        for num in tokens:
            if num == "+":
                res = stack[-2] + stack[-1]
                stack.append(res)
            elif num == "-":
                res = stack[-2] - stack[-1]
                stack.append(res)
            elif num == "*":
                res = stack[-2] * stack[-1]
                stack.append(res)
            elif num == "/":
                res = stack[-2] / stack[-1]
                stack.append(res)
            else :
                stack.append(int(num))
        return int(res)


        