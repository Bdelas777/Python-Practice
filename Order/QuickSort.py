def quick_sort(arr):
    if len(arr) <= 1:
        # if the array contains 0 or 1 element, it's already sorted
        return arr
    pivot = arr[len(arr) // 2] # select a pivot as a middle element
    left = [x for x in arr if x < pivot] # elements less than `pivot`
    middle = [x for x in arr if x == pivot] # elements equal to `pivot`
    right = [x for x in arr if x > pivot] # elements larger than `pivot`
    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([9, 7, 5, 11, 12, 2, 14, 3, 10, 6]))

# Outputs: [2, 3, 5, 6, 7, 9, 10, 11, 12, 14]