class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        trios = []
        nums.sort()
        # [-1,0,1,2,-1,-4] -> [-4,-1,-1, 0, 1, 2]

        for index, a in enumerate(nums):
            if index > 0 and a == nums[index - 1]:
                continue

            l, r = index + 1, size - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    trios.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    # (Opcional) Pula duplicados do direito para acelerar
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return trios
