class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        colder = []
        for curr_idx, curr_temp in enumerate(temperatures):
            while colder and curr_temp > colder[-1][1]:
                idx, temp = colder.pop()
                result[idx] = curr_idx - idx
            colder.append((curr_idx, curr_temp))
        return result