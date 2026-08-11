from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt_s = Counter(s)  
        cnt_t = Counter(t)
        if cnt_s == cnt_t:
            return True 
        return False