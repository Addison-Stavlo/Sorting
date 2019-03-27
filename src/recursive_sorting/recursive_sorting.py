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


# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr


# def merge_sort_in_place(arr, l, r):
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort(arr):

#     return arr
