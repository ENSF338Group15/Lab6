# 4. Searching a sorted binary tree is faster than searching a shuffled binary tree. Searching a sorted binary
#    tree ensures that it is balanced, with the search operation time complexity being O(log(n)). The shuffled
#    tree may be unbalanced, so the search operation may not have a time complexity of O(log(n)).

import timeit
import random

class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right

def insert(data, root=None):
    current = root
    parent = None

    while current is not None:
        parent = current
        if data <= current.data:
            current = current.left
        else:
            current = current.right
    if root is None:
        root = Node(data)
    elif data <= parent.data:
        parent.left = Node(data, parent)
    else:
        parent.right = Node(data, parent)
    return root  

def search(data, root):
    current = root
    while current is not None:
        if data == current.data: return current
        elif data < current.data: current = current.left
        else: current = current.right
    return None

def generate_sorted_vector(size=10000):
    return sorted(random.sample(range(1, 100000), size))

def build_tree(sorted_vector):
    root = None
    for element in sorted_vector:
        root = insert(element, root)  
    return root

def measure_search_performance(root, search_vector):
    times = []
    for element in search_vector:
        avg_time = timeit.timeit(lambda: search(element, root), number=10) / 10
        times.append(avg_time)
    total_time = sum(times)
    average_time = total_time / len(search_vector)
    return average_time, total_time

sorted_vector = generate_sorted_vector()
root = build_tree(sorted_vector)
average_time_sorted, total_time_sorted = measure_search_performance(root, sorted_vector)

shuffled_vector = sorted_vector.copy()
random.shuffle(shuffled_vector)
average_time_shuffled, total_time_shuffled = measure_search_performance(root, shuffled_vector)

print("Average time to search each element:", average_time_sorted)
print("Total time to search:", total_time_sorted)

print("Average time to search each element after shuffling:", average_time_shuffled)
print("Total time time to search after shuffling:", total_time_shuffled)
