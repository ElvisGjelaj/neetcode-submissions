class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_stack = []
        for p,s in sorted(zip(position, speed), reverse=True):
            time = (target - p) / s
            time_stack.append(time)
            if len(time_stack) >= 2 and time_stack[-2] <= time_stack[-1]:
                time_stack.pop()
        return len(time_stack)