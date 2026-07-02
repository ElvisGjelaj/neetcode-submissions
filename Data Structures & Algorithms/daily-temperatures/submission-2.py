class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        colder = []
        for curr_idx, curr_temp in enumerate(temperatures):
            if colder:
                for (idx, temp) in reversed(colder):
                    if temp < curr_temp:
                        result[idx] = curr_idx - idx
                        print(curr_temp)
                        colder.pop()
            colder.append((curr_idx, curr_temp))
        return result