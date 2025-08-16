def exclusive_products(inventory1, inventory2):
    set1 = {item.lower() for item in inventory1}
    set2 = {item.lower() for item in inventory2}

    exclusive1 = set1 - set2
    exclusive2 = set2 - set1

    result1 = sorted({item.upper() for item in inventory1 if item.lower() in exclusive1})
    result2 = sorted({item.upper() for item in inventory2 if item.lower() in exclusive2})

    return (result1, result2)

# Tests
inventory1 = ["Shirt", "Jeans", "Hat"]
inventory2 = ["jeans", "Belt", "Boots"]
print(exclusive_products(inventory1, inventory2))
# Expected: (['HAT', 'SHIRT'], ['BELT', 'BOOTS'])

inventory1 = ["T-Shirt", "hoodie", "Backpack"]
inventory2 = ["Backpack", "Hoodie", "t-shirt"]
print(exclusive_products(inventory1, inventory2))
# Expected: ([], [])

inventory1 = []
inventory2 = ["Dress", "Skirt", "Coat"]
print(exclusive_products(inventory1, inventory2))
# Expected: ([], ['COAT', 'DRESS', 'SKIRT'])
