# TO-DO: complete the helpe function below to merge 2 sorted arrays


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr

    else:
        midpoint = len(arr) // 2
        left_array = arr[:midpoint]
        right_array = arr[midpoint:]
        return(merge(merge_sort(left_array), merge_sort(right_array)))
    return arr

def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    
    index_a = 0
    index_b = 0

    for i in range(elements):
        if index_a >= len(arrA):
            merged_arr[i] = arrB[index_b]
            index_b +=1
        elif index_b >= len(arrB):
            merged_arr[i] =arrA[index_a]
            index_a += 1
        elif arrA[index_a] < arrB[index_b]:
            merged_arr[i] = arrA[index_a]
            index_a += 1
        else:
            merged_arr[i] = arrB[index_b]
            index_b += 1

    return merged_arr
# # STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr

# def merge_sort_in_place(arr, l, r): 
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

#     return arr

hello = [1,7,9,3,5,6,2]

print(merge_sort(hello))