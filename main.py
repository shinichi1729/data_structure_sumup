import sys
from typing import Optional


class MaxHeap(object):
    def __init__(self) -> None:
        self.heap = [sys.maxsize]
        self.current_size = 0

    def parent_index(self, index) -> int:
        return index // 2

    def left_child_index(self, index) -> int:
        return index * 2

    def right_child_index(self, index) -> int:
        return index * 2 + 1

    def swap(self, index1, index2) -> None:
        assert 1 <= index1 <= self.current_size
        assert 1 <= index2 <= self.current_size
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def heapify_up(self, index) -> None:
        while self.parent_index(index) > 0:
            if self.heap[index] > self.heap[self.parent_index(index)]:
                self.swap(index, self.parent_index(index))
            index = self.parent_index(index)

    def push(self, value) -> None:
        self.heap.append(value)
        self.current_size += 1
        self.heapify_up(self.current_size)

    def max_child_index(self, index) -> Optional[int]:
        if self.left_child_index(index) > self.current_size:
            return
        if self.right_child_index(index) > self.current_size:
            return self.left_child_index(index)
        if self.heap[self.left_child_index(index)] >= \
            self.heap[self.right_child_index(index)]:
            return self.left_child_index(index)
        return self.right_child_index(index)

    def heapify_down(self, index) -> None:
        while self.left_child_index(index) <= self.current_size:
            max_child_index = self.max_child_index(index)
            if self.heap[index] < self.heap[max_child_index]:
                self.swap(index, max_child_index)
            else:
                break
            index = max_child_index

    def pop(self) -> Optional[int]:
        if self.current_size < 1:
            return

        root = self.heap[1]
        data = self.heap.pop()
        if len(self.heap) == 1:
            return root

        self.heap[1] = data
        self.current_size -= 1
        self.heapify_down(1)
        return root

if __name__ == '__main__':
    max_heap = MaxHeap()
    max_heap.push(3)
    max_heap.push(7)
    max_heap.push(2)
    max_heap.push(9)
    max_heap.push(4)
    max_heap.push(5)
    max_heap.push(1)
    max_heap.push(11)
    max_heap.push(8)
    print(max_heap.heap)
