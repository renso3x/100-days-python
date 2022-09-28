def linear_search(list, target):
    """
    Returns the index position of the target if found, else return None
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [x for x in range(0, 11)]
result = linear_search(numbers, 6)
verify(result)

result = linear_search(numbers, 10)
verify(result)

result = linear_search(numbers, 12)
verify(result)