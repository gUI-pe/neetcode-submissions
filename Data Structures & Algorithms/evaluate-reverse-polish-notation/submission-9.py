import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}

        for char in tokens: 
            if char in operators:
                if char == "+":
                    stack[-2] = stack[-2] + stack[-1]
                    stack.pop()
                elif char == "-":
                    stack[-2] = stack[-2] - stack[-1]
                    stack.pop()
                elif char == "*":
                    stack[-2] = stack[-2] * stack[-1]
                    stack.pop()
                elif char == "/":
                    stack[-2] = int(stack[-2] / stack[-1])
                    stack.pop()
            else:
                stack.append(int(char))
        return stack.pop()