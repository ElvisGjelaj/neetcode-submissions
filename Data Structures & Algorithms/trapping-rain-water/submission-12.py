class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        leftMax, rightMax = [0] * length, [0] * length 
        leftMax[0], rightMax[length - 1] = height[0], height[length - 1]
        rain = 0

        for i in range(1, length):
            leftMax[i] = max(leftMax[i - 1], height[i])

        for i in range(length - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        for i in range(0, length):
            rain_above = min(leftMax[i], rightMax[i]) - height[i]
            rain += rain_above
        return rain



