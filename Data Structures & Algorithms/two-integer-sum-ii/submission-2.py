class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers) - 1

        for i in range(length - 1, -1, -1):
            j = i - 1
            if numbers[i] > target:
                continue
            while j > -1:
                if numbers[i] + numbers[j] == target:
                    return [j + 1, i + 1]
                j -= 1
        