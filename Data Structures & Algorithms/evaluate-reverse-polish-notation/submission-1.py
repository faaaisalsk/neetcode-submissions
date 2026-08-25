class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0
        for t in tokens:
            if t == "+":
                ans = stack[-2] + stack[-1]
                stack.pop(-1)
                stack.pop(-1)
                stack.append(ans)
                ans = 0
            elif t == "-":
                ans = stack[-2] - stack[-1]
                stack.pop(-1)
                stack.pop(-1)
                stack.append(ans)
                ans = 0
            elif t == "*":
                ans = stack[-1] * stack[-2]
                stack.pop(-1)
                stack.pop(-1)
                stack.append(ans)
                ans = 0
            elif t == "/":
                ans = int(stack[-2] / stack[-1])
                stack.pop(-1)
                stack.pop(-1)
                stack.append(ans)
                ans = 0
            else:
                stack.append(int(t))
        return stack[-1]