class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        end_ptr = len(nums) - 1
        k = 0
        end_loop = False
        for idx, num in enumerate(nums):
            while nums[end_ptr] == val:
                end_ptr -= 1
                if end_ptr < 1:
                    end_loop is True
            if end_loop is True:
                break
            nums[idx] = nums[end_ptr]
            nums[end_ptr] = "_"
            k += 1
        return k