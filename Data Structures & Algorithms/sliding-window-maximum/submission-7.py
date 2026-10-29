from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  
        res = []
        for r, x in enumerate(nums):
            # Drop smaller elements from the back
            while dq and nums[dq[-1]] <= x:
                dq.pop()
            dq.append(r)

            # Drop the front if it has slid out of the window
            if dq[0] <= r - k:
                dq.popleft()

            # Record the max once the first full window is formed
            if r >= k - 1:
                res.append(nums[dq[0]])
        return res