def quicksort(list):
    """
    Is faster than selection sort
    """
    if len(list) <= 1:
        return list

    less_than_pivot = []
    greater_than_pivot = []
    pivot = list[0]

    for value in list[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)


    print("%15s %ls %-15s" % (less_than_pivot, pivot, greater_than_pivot))
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


list = [4,2,10,95,33,55]
print(quicksort(list))