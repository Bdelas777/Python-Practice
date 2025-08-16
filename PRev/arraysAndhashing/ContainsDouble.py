# The same O(n) solution using a set
# to track duplicates.
def hasDuplicate(nums):
    duplicate = []
    for i in nums:
        if i not in duplicate:
            duplicate.append(i)
        else:
             return True
    return False

def hasDuplicate2(nums):
    return len(nums) != len(set(nums))

print(hasDuplicate([1, 2, 3, 4, 5, 1]))
print(hasDuplicate2([1, 2, 3, 4, 5, 1]))