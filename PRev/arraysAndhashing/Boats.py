def numRescueBoats( people, limit):
    people.sort()
    boats = 0
    i, j = 0, len(people) - 1
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
        boats += 1
    return boats

print(numRescueBoats([1,3,2,3,2],3))