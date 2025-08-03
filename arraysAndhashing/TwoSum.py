class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap  = {}
        for i, n in enumerate(nums):
            diff = target - n 
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i


# Arrays, linked lists, stacks, and queues: Understand their basic operations and implementations.  

# Trees: Basic concepts of binary trees and binary search trees.  

# Hash Tables: Basic understanding of hashing and basic hash table operations.  

# Algorithms:  

# Basic sorting and searching algorithms (e.g., bubble sort, insertion sort, linear search).  

# Basic understanding of recursion.  

# Simple dynamic programming problems.  

# Basic understanding of greedy algorithms.  