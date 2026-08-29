class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for n in nums:
            d[n] += 1
#
        s = defaultdict(list)
        for unique_num in set(nums):
            freq = d[unique_num]
            s[freq].append(unique_num)
#        
        ans = []
        for i in range(len(nums), -1, -1):
            if len(ans) == k:
                return ans
            if s[i]:
                ans.extend(s[i])
        print(ans)
        return ans
