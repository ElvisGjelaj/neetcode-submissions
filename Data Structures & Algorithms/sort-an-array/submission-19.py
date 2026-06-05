class Solution:
    def merge(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ptr1 = 0
        ptr2 = 0
        merged_nums = [0] * (len(nums1) + len(nums2))
        for idx in range(len(nums1) + len(nums2)):
            if ptr1 >= len(nums1):
                merged_nums[idx:] = nums2[ptr2:]
                return merged_nums
            if ptr2 >= len(nums2):
                merged_nums[idx:] = nums1[ptr1:]
                return merged_nums
            if nums1[ptr1] <= nums2[ptr2]:
                merged_nums[idx] = nums1[ptr1]
                ptr1 +=1
            elif nums2[ptr2] < nums1[ptr1]:
                merged_nums[idx] = nums2[ptr2]
                ptr2 +=1
        return merged_nums

    # assumes nums only has 1 or 2 elements
    def sort(self, nums):
        if len(nums) == 2:
            if nums[0] > nums[1]:
                nums[0], nums[1] = nums[1], nums[0]
        return 

    def mergesort(self, nums: List[int]) -> List[int]:
        nums_size = len(nums)
        if nums_size <= 2:
            self.sort(nums)
            return nums

        nums1 = self.mergesort(nums[: nums_size // 2])
        nums2 = self.mergesort(nums[nums_size // 2:])
        nums[:] = self.merge(nums1, nums2)
        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergesort(nums)


        
        