# TO-DO: complete the helpe function below to merge 2 sorted arrays


def merge(arrA, arrB):
    merged_arr = []
    # TO-DO
    i = j = 0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr.append(arrA[i])
            i += 1
        else:
            merged_arr.append(arrB[j])
            j += 1

    # one list has emptied into merged_arr
    # add the remaining values of the other list to merged_arr
    if i < len(arrA):
        merged_arr += arrA[i-len(arrA):]
    elif j < len(arrB):
        merged_arr += arrB[j-len(arrB):]

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]

        arr = merge(merge_sort(left), merge_sort(right))
    return arr


# STRETCH: implement an in-place merge sort algorithm

# JUST USE MERGE FUNCTION USED IN RECURSIVE ONE!
# WE DONT NEED THESE EXTRA INPUT GARBAGES
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


# i dont want l or r as inputs, thats stupid
# these are things we can tell from receiving arr
# making them required inputs is redundant
# im setting them equal to empty lists instead of removing for test file purposes
# they will be unused
def merge_sort_in_place(arr, l=[], r=[]):
    # TO-DO
    if len(arr) < 2:
        return arr

    arr_split = []
    # split array into list of divided parts
    for item in arr:
        arr_split.append([item])

    # while we are still divided
    while len(arr_split[0]) < len(arr):
        i = 0
        # loop through and merge adjacent elements
        while i < len(arr_split) - 1:
            merged_section = merge(arr_split[i], arr_split[i+1])
            # replace i-th element with merged section
            arr_split[i] = merged_section
            # delete i+1-th element now that it is in i-th
            del arr_split[i+1]
            i += 1

    return arr_split[0]


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt

# helper for timsort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and temp < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = temp

    return arr


def timsort(arr):

    sorted_arrs = []
    # break array up into segments (size 32)
    # sort these segments using insertion sort
    # place sorted segments in sorted_arrs for safe keeping
    for i in range(0, len(arr), 32):
        sorted_sub_arr = insertion_sort(arr[i:min(i+32, len(arr))])
        sorted_arrs.append(sorted_sub_arr)

    # now essentially copy the last half of merge_sort_in_place above
    # merge together all the sorted sub arrays until there is nothing left to merge
    while len(sorted_arrs[0]) < len(arr):
        i = 0
        # loop through and merge adjacent elements
        while i < len(sorted_arrs) - 1:
            merged_section = merge(sorted_arrs[i], sorted_arrs[i+1])
            # replace i-th element with merged section
            sorted_arrs[i] = merged_section
            # delete i+1-th element now that it is in i-th
            del sorted_arrs[i+1]
            i += 1

    return sorted_arrs[0]
