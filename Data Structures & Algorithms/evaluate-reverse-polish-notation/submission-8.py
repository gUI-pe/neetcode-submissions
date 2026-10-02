import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        #print(tokens)

        for char in tokens: 
            #print(char)
            if char in operators:
                #print("entrou operators")
                #print(stack)
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
                    #print(stack[-2], stack[-1])
                    stack[-2] = int(stack[-2] / stack[-1])
                    stack.pop()
                #print(stack)
            else:
                #print("entrou em add")
                stack.append(int(char))
        return stack.pop()