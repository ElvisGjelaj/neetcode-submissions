class MinStack:

    def __init__(self):
        self.stack = [None]
        self.min = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min or self.min < val:
            self.min = val

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
