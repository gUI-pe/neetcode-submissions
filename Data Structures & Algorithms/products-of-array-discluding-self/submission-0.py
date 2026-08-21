class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        global_answer = 1
        zeros = 0
        zero_answer = False

        while(zeros < 2): 
            for n in nums:
                if n == 0:
                    zeros += 1
                    zero_answer = True
                else:
                    global_answer *= n
            break 

        for index, n in enumerate(nums):
            if zero_answer == True and (zeros >= 2 or n != 0):
                nums[index] = 0
            elif zero_answer == True:
                nums[index] = global_answer
            elif zero_answer == False:
                nums[index] = int(global_answer / n)



        return nums