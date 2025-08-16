def binary_search_iterative(data, target):
    # We will search in the interval [low, high), where the right border is excluded
    low = 0
    high = len(data)

    while high - low > 1: # search until the length of the interval > 1
        mid = (low + high) // 2
        if target < data[mid]:
            high = mid # Continue our search in [low, mid)
        else:
            low = mid # Continue our search in [mid, high)
    return low if data[low] == target else None