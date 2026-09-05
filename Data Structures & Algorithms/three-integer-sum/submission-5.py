from collections import defaultdict
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        trios = set()  # set() garante busca e inserção em O(1)
        nums_hash = defaultdict(list)

        for index, n in enumerate(nums):
            nums_hash[n].append(index)

        for i in range(size - 1):
            for j in range(i + 1, size):
                diff = -(nums[i] + nums[j])
                
                if diff in nums_hash:
                    for k in nums_hash[diff]:
                        # k > j já garante que k != i e k != j automaticamente
                        if k > j:
                            trio = tuple(sorted([nums[i], nums[j], nums[k]]))
                            trios.add(trio)

        # Converte o conjunto de tuplas de volta para lista de listas
        return [list(t) for t in trios]