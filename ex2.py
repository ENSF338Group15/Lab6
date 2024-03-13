# 4. Binary search on a sorted array is faster than searching a binary search tree. Binary search on a sorted array
#    has a search operation time complexity being O(log(n)). On the other hand, the binary search tree could be unbalanced, 
#    where the search operation may not have a time complexity of O(log(n)) but O(n) instead.

import timeit
import random

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_recursive(data, self.root)

    def insert_recursive(self, data, node):
        if data <= node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert_recursive(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert_recursive(data, node.right)

    def search_recursive(self, data, node):
        if node is None or node.data == data:
            return node
        elif data < node.data:
            return self.search_recursive(data, node.left)
        else:
            return self.search_recursive(data, node.right)
        
    def search(self, data):
        return self.search_recursive(data, self.root) if self.root else None

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def generate_sorted_vector(size=10000):
    return sorted(random.sample(range(1, 100000), size))

def measure_bst_performance(sorted_vector):
    bst = BinarySearchTree()
    for element in sorted_vector:
        bst.insert(element)

    times_bst = []
    for element in sorted_vector:
        avg_time = timeit.timeit(lambda: bst.search(element), number=10) / 10
        times_bst.append(avg_time)
    total_time_bst = sum(times_bst)
    average_time_bst = total_time_bst / len(sorted_vector)
    return average_time_bst, total_time_bst

def measure_binary_search_performance(sorted_vector):
    sorted_vector.sort()
    times_binary_search = []
    for element in sorted_vector:
        avg_time = timeit.timeit(lambda: binary_search(sorted_vector, element), number=10) / 10
        times_binary_search.append(avg_time)
    total_time_binary_search = sum(times_binary_search)
    average_time_binary_search = total_time_binary_search / len(sorted_vector)
    return average_time_binary_search, total_time_binary_search

sorted_vector = generate_sorted_vector()

shuffled_vector = sorted_vector.copy()
random.shuffle(shuffled_vector)

average_time_bst, total_time_bst = measure_bst_performance(shuffled_vector)
average_time_binary_search, total_time_binary_search = measure_binary_search_performance(shuffled_vector)

print("Average time to search each element in the Binary Seach Tree:", average_time_bst)
print("Total time to search in the Binary Seach Tree:", total_time_bst)

print("Average time to binary search on a sorted array each element:", average_time_binary_search)
print("Total time to binary search on a sorted array:", total_time_bst)

# Used ChatGPT to generate BinarySearchTree 
