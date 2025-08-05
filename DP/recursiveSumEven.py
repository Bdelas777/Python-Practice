def recursiveSumEven(arr, idx=0):
    if idx == len(arr):
        return 0
    current = arr[idx]
    if current % 2 == 0:
        return current + recursiveSumEven(arr, idx + 1)
    else:
        return recursiveSumEven(arr, idx + 1)


# Testing the function
print(recursiveSumEven([1, 2, 3, 4, 5, 6])) # Expected output: 9
print(recursiveSumEven([2, 3])) # Expected output: 2
print(recursiveSumEven([])) # Expected output: 0    