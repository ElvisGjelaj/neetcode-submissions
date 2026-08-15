class Solution:
    def getPeaks(self, heights: List[int]) -> List[bool]:
        peaks = []
        if len(heights) == 1:
            return [False]
        for idx, height in enumerate(heights):
            if idx == 0:
                if height > heights[idx + 1]:
                    peaks.append(True)
                else: 
                    peaks.append(False)
            elif idx == len(heights) - 1:
                if height > heights[idx - 1]:
                    peaks.append(True)
                else: 
                    peaks.append(False)
            else:
                if height < heights[idx - 1] and height > heights[idx + 1]:
                    peaks.append(True)
                else: 
                    peaks.append(False) 
        return peaks

    def trap(self, heights: List[int]) -> int:
        peaks = self.getPeaks(heights)
        max_rain = 0
        for left, height in enumerate(heights):
            if not peaks[left]:
                continue
            right = peaks.index(True, left)
            rain = (right - left) * min(heights[left], heights[right])
            for col in range(right - 1, left, -1):
                rain -= heights[col]
            max_rain += rain
        
        return max_rain
            









