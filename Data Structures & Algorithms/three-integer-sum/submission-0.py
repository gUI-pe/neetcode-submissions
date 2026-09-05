class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        trios = set([])
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    soma = nums[i] + nums[j] + nums[k]
                    if soma == 0:
                        trio = tuple(sorted([nums[i], nums[j], nums[k]]))
                        trios.add(trio)                        
                        if trio not in trios:
                            trios.append(trio)
        return(list(trios))