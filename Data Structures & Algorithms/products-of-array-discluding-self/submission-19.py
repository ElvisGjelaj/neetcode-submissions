class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = [1] * length
        right = [1] * length

        for idx in range(1, length):
            left[idx] = left[idx - 1] * nums[idx - 1]
        for idx in range(length - 2, -1, -1):
            right[idx] = right[idx + 1] * nums[idx + 1]
        
        excepted = [0] * length
        for idx in range(length):
            excepted[idx] = left[idx ] * right[idx]
        
        return excepted

