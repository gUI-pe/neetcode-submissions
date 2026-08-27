class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = defaultdict(int)
        longest = 0

        for n in nums:
            d[n] = 1
        
        
        for n in nums:
            if (n - 1) not in d:
                while (n + 1) in d:
                    d[n + 1] = d[n] + 1
                    n += 1
                longest = max(longest, d[n])   
        return longest