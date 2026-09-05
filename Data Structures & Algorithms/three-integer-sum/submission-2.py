class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        trios = []
        nums_hash = defaultdict(list)
        for index, n in enumerate(nums):
            nums_hash[n].append(index)

        #print(nums_hash) 

        #fazer a soma de todas as duplas
        for i in range(size - 1):
            for j in range(i + 1, size):
                soma = nums[i] + nums[j]
                diff = 0 - soma
                #print(diff)
                if diff in nums_hash:
                    #print(diff, "encontrada no hash")
                    for indexes in nums_hash[diff]:
                        #print("indices de diff: ",nums_hash[diff])
                        if indexes != i and indexes != j and tuple(sorted([nums[i], nums[j], nums[indexes]])) not in trios:
                            #print("adicionando: ", [nums[i], nums[j], nums[indexes]])
                            trio = tuple(sorted([nums[i], nums[j], nums[indexes]]))
                            trios.append(trio)


        return(trios)