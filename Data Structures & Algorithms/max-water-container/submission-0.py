class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right: 
            if heights[left] < heights[right]:
                curr_area = (right - left) * heights[left]
                left += 1
            else: 
                curr_area = (right - left) * heights[right]
                right -= 1
            if curr_area > max_area:
                 max_area = curr_area
        return max_area
