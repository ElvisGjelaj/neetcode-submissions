class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0

        while left < right: 
            if heights[left] < heights[right]:
                curr_area = (right - left) * heights[left]
                left += 1
            else: 
                curr_area = (right - left) * heights[right]
                right -= 1
            max_area = max(curr_area, max_area)
            
        return max_area
