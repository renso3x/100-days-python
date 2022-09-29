def binary_search(list, target):
    """
    Only works with sorted list, same as linear search
    """
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last)//2 #rounds down to the nearest number
        
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [x for x in range(0, 11)]
result = binary_search(numbers, 3)
verify(result)

result = binary_search(numbers, 8)
verify(result)

result = binary_search(numbers, 12)
verify(result)