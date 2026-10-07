class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_sz = len(nums)
        curr_product = 1
        
        left = [1] * nums_sz
        right = [1] * nums_sz
        res = [0] * nums_sz

        for i in range(1, nums_sz):
            curr_product = curr_product * nums[i - 1]
            left[i] = curr_product
        
        curr_product = 1

        for i in range(nums_sz - 2, -1 , -1):
            curr_product = curr_product * nums[i + 1]
            right[i] = curr_product
        
        for i in range(0, nums_sz):
            res[i] = left[i] * right[i]

        return res
