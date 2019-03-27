# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []
    # TO-DO
    for i in range(min([len(arrA), len(arrB)])):
        if arrA[i] < arrB[i]:
            merged_arr.append(arrA[i])
            merged_arr.append(arrB[i])
        else:
            merged_arr.append(arrB[i])
            merged_arr.append(arrA[i])

    # compensate for lists not being same length
    difference = len(arrA) - len(arrB)
    if difference > 0:
        # add the remaining amount of arrA
        merged_arr += arrA[-difference:]
    elif difference < 0:
        merged_arr += arrB[difference:]

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]

        arr1 = merge_sort(left)
        arr2 = merge_sort(right)

        arr = merge(arr1, arr2)
    return arr


print(merge([3, 5, 7, 8, 9], [1, 2, 6, 10]))
print(merge_sort([5, 6, 4, 3, 8, 9, 0, 1, 2, 3, 5, 3, 7]))
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
