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


def timsort(arr):

    return arr
