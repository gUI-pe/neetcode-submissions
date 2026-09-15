class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0]*len(height)
        max_right = [0]*len(height)
        
        curr_max = 0
        for i, value in enumerate(height):
            max_left[i] = curr_max
            curr_max = max(curr_max, value)

        curr_max = 0
        for i in range(len(height) - 1, -1, -1):
            max_right[i] = curr_max
            curr_max = max(curr_max, height[i])

        res = 0
        for i in range(len(height)):
            water = min(max_left[i], max_right[i]) - height[i]
            if water > 0:
                res += water
        return res