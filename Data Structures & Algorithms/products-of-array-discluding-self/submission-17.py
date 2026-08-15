class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = [1] * length
        right = [1] * length

        for idx in range(1, length):
            left[idx] = left[idx - 1] * nums[idx - 1]
        for idx in range(length - 2, -1, -1):
            right[idx] = right[idx + 1] * nums[idx - 1]
        
        excepted = [0] * length
        for idx in range(length):
            if idx == 0:
                excepted[idx] = right[idx + 1]
            if idx == length - 1:
                excepted[idx] = left[idx - 1]
            else: excepted[idx] = left[idx - 1] * right[idx + 1]
        
        return excepted

