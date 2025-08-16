def search_dec_rotated(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        
        # Lado izquierdo ordenado descendente
        if nums[left] >= nums[mid]:
            if nums[left] >= target > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Lado derecho ordenado descendente
        else:
            if nums[mid] > target >= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


print(search_dec_rotated([4, 3, 2, 1, 8, 7, 6, 5], 1))  # Expected output: 3
print(search_dec_rotated([9, 8, 7, 6, 5, 4, 3, 2, 1], 4))  # Expected output: 5
print(search_dec_rotated([5, 4, 3, 2, 1], 8))  # Expected output: -1