class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        biggest_rect = 0
        for idx, curr_height in enumerate(heights):
            #check left
            l = idx
            while l > -1:
                if heights[l] >= curr_height:
                    if l == 0 or heights[l - 1] < curr_height:
                        break
                    l -= 1

            #check right
            r = idx
            while r < len(heights):
                if heights[r] >= curr_height:
                    if r == (len(heights) - 1) or heights[r + 1] < curr_height:
                        break
                    r += 1

            #compare rect area
            curr_rect = curr_height * (r - l + 1)
            if curr_rect > biggest_rect:
                biggest_rect = curr_rect
        return biggest_rect
