class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []  # Cria uma lista vazia

        for c in s:
            if c.isalnum():
                chars.append(c.lower())  # O(1) amortizado por caractere

        newStr = "".join(chars)  # Une toda a lista em uma única string em O(N)

        return newStr == newStr[::-1]