import heapq
import timeit
import random
from typing import List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class ListPriorityQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, value):
        new_node = Node(value)
        if not self.head or value < self.head.value:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            while curr.next and curr.next.value < value:
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node

    def dequeue(self):
        if self.head:
            value = self.head.value
            self.head = self.head.next
            return value

class HeapPriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, value):
        heapq.heappush(self.heap, value)

    def dequeue(self):
        return heapq.heappop(self.heap) if self.heap else None

def measure_time(queue, tasks: List[bool]):
    start_time = timeit.default_timer()
    for task in tasks:
        if task:  # enqueue
            queue.enqueue(random.randint(1, 1000))
        else:  # dequeue
            queue.dequeue()
    end_time = timeit.default_timer()
    return end_time - start_time

tasks = [random.random() < 0.7 for _ in range(1000)]
list_queue = ListPriorityQueue()
heap_queue = HeapPriorityQueue()

list_time = measure_time(list_queue, tasks)
heap_time = measure_time(heap_queue, tasks)

print(f"ListPriorityQueue time: {list_time}")
print(f"HeapPriorityQueue time: {heap_time}")

# Answer to exercise 5, question 4:
# From observating the times, it is clear that HeapPriorityQueue implementation has the better performance from the faster
# time. This is because of the HeapPriorityQueue uses a binary heap, a complete binary tree and the dequeue operation heapq.heapop.
# Both the usage of the binary tree and the dequeue operation have a time complexity of O(log n). Compared to the ListPriorityQueue
# which uses a linked list, and the enqueue operation involves inserting an element in the correct position, which requires transversing
# the entire list resulting in a time complexity of O(n). The dequeue operation is simply O(1) as it removes the first element, however
# when comparing the time complexities of the both implementations, the HeapPriorityQueue will have the better time complexity and thus
# better performance.
