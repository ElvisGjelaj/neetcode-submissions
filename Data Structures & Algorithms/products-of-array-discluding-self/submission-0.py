class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = [nums[0]] * length
        right = [length - 1] * length
        for l_idx, num in enumerate(nums):
            r_idx = length - idx
            if idx != 0:
                left[l_idx] = left[l_idx - 1] * num
                right[r_idx] = right[r_idx + 1] * nums[r_idx]
        
        excepted = [0] * length
        for idx in range(length):
            if idx == 0:
                excepted[idx] = right[idx + 1]
            if idx == length - 1:
                excepted[idx] = left[idx - 1]
            else: excepted[idx] = left[idx - 1] * right[idx + 1]
            

