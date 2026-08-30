class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Pre-process the string (strip non-alphanumeric and lowercase)
        filtered = [c.lower() for c in s if c.isalnum()]
        
        n = len(filtered)
        for i in range(n // 2):
            if filtered[i] != filtered[n - 1 - i]:
                return False
        return True