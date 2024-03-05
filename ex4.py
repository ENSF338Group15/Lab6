import heapq

class Heap:
    def __init__(self):
        self.heap = []

    def heapify(self, arr):
        self.heap = arr
        heapq.heapify(self.heap)

    def enqueue(self, item):
        heapq.heappush(self.heap, item)

    def dequeue(self):
        return heapq.heappop(self.heap)

# Helper function to check if a list is a valid heap
def is_heap(h):
    n = len(h)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and h[i] > h[left]:
            return False
        if right < n and h[i] > h[right]:
            return False
    return True

# Unit Tests
def test_heap():
    # Test case 1: Input array is already a correctly sorted heap
    h = Heap()
    h.heapify([1, 2, 3, 4, 5])
    assert h.heap == [1, 2, 3, 4, 5]

    # Test case 2: Input array is empty
    h = Heap()
    h.heapify([])
    assert h.heap == []

    # Test case 3: Input array is a long, randomly shuffled list of integers
    h = Heap()
    h.heapify([9, 3, 5, 2, 8, 10, 6, 1, 4, 7])
    assert is_heap(h.heap)  # Check if the output is a valid heap

test_heap()