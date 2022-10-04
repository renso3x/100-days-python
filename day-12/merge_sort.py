def merge_sort(list):
    """
    Sorts a list in asecending order
    Returns a new sorted list

    1. Divide: Find the midpoint of the list and divide into sublist
    
    2. Conquer: Recursively sort the sublist created in previous set
    
    3. Combine: Merge the sorted sublist created in previous set

    Takes O(n log n) time -> Expensive
    """
    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublist - left and right
    
    Takes overall O(log n) time
    """
    midpoint = len(list)//2
    left = list[:midpoint]
    right = list[midpoint:]

    return left, right

def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list

    Takes overall O(n log n) time -> O(n)
    """

    l = []
    i = 0
    j = 0

    # Conditions for equal length of sub list 
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1
    
    while j < len(right):
        l.append(right[j])
        j += 1

    return l

def verify_sorted(list):
    n = len(list)
    
    if n == 0 or n == 1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])


alist = [100,99,98,80,82,77,200]
sorted_list = merge_sort(alist)
print(verify_sorted(sorted_list))