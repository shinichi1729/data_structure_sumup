import sys
import numpy as np


class MiniHeap(object):
    def __init__(self):
        self.heap = [-sys.maxsize]
        self.current_size = 0

    def parent_index(self, index: int) -> int:
        return index // 2

    def left_child_index(self, index: int) -> int:
        return index * 2

    def right_child_index(self, index: int) -> int:
        return index * 2 + 1

    def swap(self, index1: int, index2: int) -> None:
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def heapify_up(self, index: int) -> None:
        while self.parent_index(index) > 0:
            if self.heap[index] < self.heap[self.parent_index(index)]:
                self.swap(index, self.parent_index(index))
            index = self.parent_index(index)

    def add(self, value: int) -> None:
        self.heap.append(value)
        self.current_size += 1
        self.heapify_up(self.current_size)

    def min_child_index(self, parent_index: int) -> int:
        if self.left_child_index(parent_index) > self.current_size:
            return
        elif self.right_child_index(parent_index) > self.current_size:
            return self.left_child_index(parent_index)
        else:
            if (self.heap[self.left_child_index(parent_index)] <
                    self.heap[self.right_child_index(parent_index)]):
                return self.left_child_index(parent_index)
            else:
                return self.right_child_index(parent_index)

    def heapify_down(self, index: int) -> None:
        while self.left_child_index(index) < self.current_size:
            min_child_index = self.min_child_index(index)
            if self.heap[index] > self.heap[min_child_index]:
                self.swap(index, min_child_index)
            index = min_child_index

    def pop(self) -> int:
        if self.current_size == 1:
            return
        root = self.heap[1]
        data = self.heap.pop()
        if len(self.heap) == 1:
            return

        self.heap[1] = data
        self.heapify_down(1)
        return root

    def __str__(self):
        lines = []
        current_size_log = int(np.log2(self.current_size))
        for i in range(0, current_size_log+1):
            lines.append(self.heap[2 ** i: 2 ** (i+1)])
        return '\n'.join(f'{line}' for line in lines)


if __name__ == '__main__':
    min_heap = MiniHeap()
    min_heap.add(5)
    min_heap.add(6)
    min_heap.add(3)
    min_heap.add(8)
    min_heap.add(11)
    min_heap.add(1)
    print(min_heap)
