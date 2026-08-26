class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = defaultdict(int)
        longest = 0

        for n in nums:
            d[n] = 1
        
        print(len(d.keys()))
        while(len(d.keys()) > 0):
            key = next(iter(d))
            
            while (key - 1) in d:
                key -= 1
            
            while (key + 1) in d:
                d[key + 1] = d[key] + 1
                d.pop(key)
                key += 1
            longest = max(longest, d[key])
            d.pop(key)    
        return longest