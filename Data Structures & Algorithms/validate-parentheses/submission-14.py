class Solution:
    def isValid(self, s: str) -> bool:
        closers = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for char in s:
            if char in closers and stack:
                if closers[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return False if stack else True
                