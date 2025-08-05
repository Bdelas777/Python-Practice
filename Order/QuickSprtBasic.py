# Import required libraries
import random 

def partition(arr, low, high):
    # this method partitions arr[low..high] to move all elements <= arr[high] to the left
    # and returns the index of `pivot` in the updated array
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
        
# Generate a list of random numbers between 1 and 100
random_list = random.sample(range(1, 101), 20)
print('Unsorted list:', random_list)

quick_sort(random_list, 0, len(random_list) - 1)
print('Sorted list with Quick Sort:', random_list)