def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return  recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)

def verify(result):
    print("Target found: ", result)

numbers = [x for x in range(0, 11)]
result = recursive_binary_search(numbers, 6)
verify(result)

result = recursive_binary_search(numbers, 10)
verify(result)

result = recursive_binary_search(numbers, 12)
verify(result)