class Solution:
    def merge(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ptr1 = 0
        ptr2 = 0
        merged_nums = [0] * (len(num1) + len(nums2))
        for idx in range(len(nums1) + len(nums2)):
            if nums[ptr1] > nums[ptr2]:
                merged_nums[idx] = nums[ptr1]
                ptr1 +=1
            if nums[ptr2] > nums[ptr1]:
                merged_nums[idx] = nums[ptr2]
                ptr2 +=1
        return merged_nums

    # assumes nums only has 1 or 2 elements
    def sort(self, nums):
        if len(nums) > 2:
            if nums[0] > nums[1]:
                nums[0], nums[1] = nums[1], nums[0]
        return 

    def mergesort(self, nums: List[int]) -> List[int]:
        nums_size = len(nums)
        if nums_size <= 2:
            self.sort(nums)
            return nums

        num1 = self.mergesort(nums[: nums_size // 2])
        num2 = self.mergesort(nums[nums_size // 2:])
        nums[:] = self.merge(nums1, num2)
        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergesort(nums)


        
        