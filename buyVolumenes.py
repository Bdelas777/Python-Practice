def buyVolumes(volumes):
    n = len(volumes)
    result = []
    available = set()
    next_to_buy = 1
    
    for v in volumes:
        available.add(v)
        today_purchase = []
        
        while next_to_buy in available:
            today_purchase.append(next_to_buy)
            available.remove(next_to_buy)
            next_to_buy += 1
        
        if not today_purchase:
            result.append([-1])
        else:
            result.append(today_purchase)
    
    return result


# Ejemplos:
print(buyVolumes([2, 1, 4, 3]))   # [[-1], [1, 2], [-1], [3, 4]]
print(buyVolumes([1, 4, 3, 2, 5])) # [[1], [-1], [-1], [2, 3, 4], [5]]
