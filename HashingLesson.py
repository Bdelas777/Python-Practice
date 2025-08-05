def simple_hash(input_string):
    summation = sum(ord(ch) for ch in input_string)
    return summation % 10  # We limit our hash range from 0 to 9

print(simple_hash('Hello'))  # outputs: 0
print(simple_hash('world'))  # outputs: 2

# Define a set
student_ids = set()

# Add elements
student_ids.add(123)
student_ids.add(456)
student_ids.add(789)

# Check existence
print(456 in student_ids)  # Outputs: True
print(111 in student_ids)  # Outputs: False

hash_set = set()

# Adding elements to the set
hash_set.add("element1")
hash_set.add("element1")

# Check the content of the set
print(hash_set)  # Output: {'element1'}
hash_set = set()

# Adding elements
hash_set.add("element3")
hash_set.add("element1")
hash_set.add("element2")

#Check the content of the set
print(hash_set)  # Output: {'element1', 'element2', 'element3'}
# Lookup: 
# O(1) average, O(n) worst-case.
# Insertion: 
# O(1) average, O(n) worst-case.
# Deletion: 
# O(1) average, O(n) worst-case

# Grocery list
grocery_list = set()

# Adding items
grocery_list.add('Milk')
grocery_list.add('Cheese')
grocery_list.add('Bread')

# Checking existence
print('Milk' in grocery_list)  # Outputs: True
print('Butter' in grocery_list)  # Outputs: False

# Add a new item
grocery_list.add('Butter')
print('Butter' in grocery_list)  # Outputs: True

# Try removing an item
grocery_list.remove('Bread')
print('Bread' in grocery_list)  # Outputs: False

# Clear the grocery list
grocery_list.clear()
print(grocery_list)  # Outputs: set()

# Create a new list and make a copy of it
new_list = set(['Eggs', 'Jam', 'Ham'])
copied_list = new_list.copy()

print(new_list)  # Outputs: {'Eggs', 'Ham', 'Jam'}
print(copied_list)  # Outputs: {'Eggs', 'Ham', 'Jam'}

# Modifying the copied list won't affect the original list
copied_list.remove('Ham')
print(new_list)  # Outputs: {'Eggs', 'Ham', 'Jam'}
print(copied_list)  # Outputs: {'Eggs', 'Jam'}