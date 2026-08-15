class Solution:
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        i = 0
        j = 0
        merged = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        
        return merged

    # assumes nums only has 1 or 2 elements
    def sort(self, nums):
        if len(nums) == 2:
            if nums[0] > nums[1]:
                nums[0], nums[1] = nums[1], nums[0]
        return 

    def mergesort(self, nums: List[int]) -> List[int]:
        middle = len(nums) // 2
        if nums_size <= 1:
            return nums

        left = self.mergesort(nums[: middle])
        right = self.mergesort(nums[middle:])
        nums[:] = self.merge(left, right)
        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergesort(nums)


        
        