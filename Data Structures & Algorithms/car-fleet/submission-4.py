class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        for idx, start in enumerate(position):
            print(idx, start)
            time[idx] = (target-start) / speed[idx]

        
        for idx in range(len(time) -1, 0, -1):
            if time[idx] >= time[idx -1]:
                time[idx - 1] = time[idx]
        return len(set(time))
