#bubble sort
#an algorithm to sort elements in a list
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print(my_list)

#quick sort
#an algorithm for sorting elements in a list by use of a pivot and subdivision
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]# // is floor division, in order to have the pivot index as a whole number
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    #for the return, the function quick_sort is called again to sort both the left and the right side
    return quick_sort(left) + middle + quick_sort(right)

my_list1 = [64, 34, 25, 12, 22, 11, 90, 52, 73]
sorted_list = quick_sort(my_list1)
print(sorted_list)

#binary search
#an algorithm for finding an element in a sorted list
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2 #remember floor division
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

my_list2 = sorted_list #from the previous quick_sort algorithm
target_value = 25
result = binary_search(my_list, target_value)
print(f"{my_list2[result]} found at index {result}")

#linear search
#simple search algorithm for an item in a list
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

my_list3 = sorted_list
target_value1 = 90
result1 = linear_search(my_list3, target_value1)
print(f"{my_list3[result1]} found at index {result1}")


#some algorithms I've not included in here:
#depth_first search(dfs)
#breadth_first search(bfs)
#inorder, preorder, postorder traversal

 


