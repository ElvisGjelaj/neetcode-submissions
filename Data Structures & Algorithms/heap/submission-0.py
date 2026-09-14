from typing import List

class MinHeap:
    
    def __init__(self):
        self.min_heap = []

    def push(self, val: int) -> None:
        self.min_heap.append(val)
        curr_idx = len(self.min_heap) - 1

        while curr_idx > 0:
            parent_idx = (curr_idx - 1) // 2

            if self.min_heap[curr_idx] >= self.min_heap[parent_idx]:
                break

            self.min_heap[curr_idx], self.min_heap[parent_idx] = (
                self.min_heap[parent_idx],
                self.min_heap[curr_idx]
            )

            curr_idx = parent_idx


    def pop(self) -> int:

        if not self.min_heap:
            return -1

        min_val = self.min_heap[0]

        if len(self.min_heap) == 1:
            self.min_heap.pop()
            return min_val

        self.min_heap[0] = self.min_heap.pop()
        parent_idx = 0
        heap_sz = len(self.min_heap)

        while True:
            left = (parent_idx * 2) + 1
            right = (parent_idx * 2) + 2

            if left >= heap_sz:
                break

            smaller_child = left

            if right < heap_sz and self.min_heap[right] < self.min_heap[left]:
                smaller_child = right

            if self.min_heap[parent_idx] <= self.min_heap[smaller_child]:
                break

            self.min_heap[parent_idx], self.min_heap[smaller_child] = (
                self.min_heap[smaller_child],
                self.min_heap[parent_idx]
            )

            parent_idx = smaller_child

        return min_val


    def top(self) -> int:
        if not self.min_heap:
            return -1

        return self.min_heap[0]


    def heapify(self, nums: List[int]) -> None:
        self.min_heap = []

        for num in nums:
            self.push(num)
        
        