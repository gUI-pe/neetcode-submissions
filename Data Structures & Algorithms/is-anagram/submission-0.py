class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            d = {}
            for letter in "abcdefghijklmnopqrstuvwxyz":
                d[letter] = 0
            for letter in s:
                d[letter] += 1
            for letter in t:
                d[letter] -= 1
            print(d.values())
            for values in d.values():
                if values > 0:
                    return False
            return True
        return False