# insertion sort ex from GP
def insertion_sort(books):
    for i in range(1, len(books)):
        temp = books[i]
        j = i
        while j > 0 and temp.genre < books[j - 1].genre:
            books[j] = books[j - 1]
            j -= 1
        books[j] = temp

    return books

# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    madeSwap = True

    while madeSwap:
        madeSwap = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                madeSwap = True

    return arr


print(bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))
# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):
    maximum = max(arr)

    sorted_arr = [0]*len(arr)
    counts = [0]*(maximum+1)

    # store amount of times we see each element in array
    for element in arr:
        counts[element] += 1

    # modify counts to make each count the sum of previous counts before it
    sum_of_counts = 0
    for i in range(len(counts)):
        sum_of_counts += counts[i]
        counts[i] = sum_of_counts

    # build output
    for i in range(len(arr)):
        # set location of element arr[i]
        # to be at the index of how many elements we counted before it
        sorted_arr[counts[arr[i]] - 1] = arr[i]
        # we placed one instance of that number we counted
        # subtract one so next time we insert it, it inserts 1 space to the left
        counts[(arr[i])] -= 1

    return sorted_arr


print(count_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))
