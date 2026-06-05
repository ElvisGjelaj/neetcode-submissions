class Solution:
    def makeMaxHeap(self, nums: List[int]) -> List[int]:
        for i in range((len(nums)- 1) // 2, -1, -1):
            self.Heapify(nums, i, len(nums))

    def Heapify(self, nums: List[int], idx: int, heap_size: int) -> List[int]:
        while 2 * idx + 1 < heap_size:
            left = 2 * idx + 1
            right = 2 * idx + 2
            largest = idx

            if left < heap_size and nums[left] > nums[largest]:
                largest = left
            if right < heap_size and nums[right] > nums[largest]:
                largest = right
            if largest == idx:
                break

            nums[idx], nums[largest] = nums[largest], nums[idx]
            idx = largest
        return 

    def sortArray(self, nums: List[int]) -> List[int]:
        self.makeMaxHeap(nums)
        end_ptr = len(nums) - 1
        while end_ptr > 0:
            nums[end_ptr], nums[0] = nums[0], nums[end_ptr]
            self.Heapify(nums, 0, end_ptr)
            end_ptr -=1
        return nums

        
