class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # res = 0
        for num in tokens:
            if num == "+":
                res = stack.pop() + stack.pop()
                stack.append(res)
            elif num == "-":
                a, b = stack.pop(), stack.pop()
                res = b - a
                stack.append(res)
            elif num == "*":
                res = stack.pop() * stack.pop()
                stack.append(res)
            elif num == "/":
                a, b = stack.pop(), stack.pop()
                res = int(float(b) / a)
                stack.append(res)
            else :
                stack.append(int(num))
        return int(res)


        