class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [0] * len(position)
        for idx, start in enumerate(position):
            time[idx] = (target-start) / speed[idx]

        time = [t for t, _ in sorted(zip(position, time))]
        
        for idx in range(len(time) -1, 0, -1):
            if time[idx] >= time[idx -1]:
                time[idx - 1] = time[idx]
        return len(set(time))
