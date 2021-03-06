# STRETCH: implement Linear Search
def linear_search(arr, target):
    # TO-DO: add missing code
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search


def binary_search(arr, target):
    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1
    # TO-DO: add missing code
    while low <= high:
        mid = ((high-low) // 2) + low
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search


def binary_search_recursive(arr, target, low, high):
    middle = ((high-low)//2) + low

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
    if arr[middle] == target:
        return middle
    elif arr[middle] > target:
        return binary_search_recursive(arr, target, low, middle-1)
    else:
        return binary_search_recursive(arr, target, middle+1, high)
