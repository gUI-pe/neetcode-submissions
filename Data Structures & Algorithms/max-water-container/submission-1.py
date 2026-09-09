class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        for index, value in enumerate(heights):
            for pair, pair_value in enumerate(heights):
                curr_sum = (min(value, pair_value)*(pair - index))
                max_area = max(curr_sum, max_area)
        return max_area
                    