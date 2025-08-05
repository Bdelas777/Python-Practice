def merge_sort(lst):
    # If it's a single element or an empty list, it's already sorted
    if len(lst) <= 1:
        return lst

    # Find the middle point
    mid = len(lst) // 2

    # Recursively sort both halves
    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])

    # Merge the two sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = 0
    j = 0

    # Compare the smallest unused elements in both lists and append the smallest to the result
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Once we've exhausted one list, append all remaining elements from the other list to the result
    # Here, we append both lists, as at least one is an empty list
    result.extend(left[i:])
    result.extend(right[j:])
    return result