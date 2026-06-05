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

    def mergesort(self, nums: List[int]) -> List[int]:
        middle = len(nums) // 2
        if len(nums) == 1:
            return nums

        left = self.mergesort(nums[: middle])
        right = self.mergesort(nums[middle:])
        nums[:] = self.merge(left, right)
        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergesort(nums)


        
        