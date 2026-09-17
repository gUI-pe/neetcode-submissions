class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = [")", "}", "]"]
        opening = ["(", "[", "{"]

        for char in s:
            if char in closing and len(stack) > 0:
                if stack[-1] == "(" and char == ")":
                    stack.pop()
                elif stack[-1] == "[" and char == "]":
                    stack.pop()
                elif stack[-1] == "{" and char == "}":
                    stack.pop()
                else:
                    return False
            elif char in opening:
                stack.append(char)
            else:
                return False

        if len(stack) == 0:
            return True
        return False