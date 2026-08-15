class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_stack = []
        for p,s in sorted(zip(position, speed), reverse=True):
            time = (target - p) / s
            if time_stack and time_stack[-1] <= time:
                time_stack.pop()
            time_stack.append(time)
        return len(time_stack)