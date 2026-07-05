class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        biggest_rect = 0
        stack = [] 

        for idx, height in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > height:
                i, h = stack.pop()
                curr_rect = h * (idx - i)
                biggest_rect = max(biggest_rect, curr_rect) 
                start = i
            stack.append((start, height))

        for i, h in stack:
            biggest_rect = max(biggest_rect, h * (len(heights) - i))
        return biggest_rect
