def smallest_element(arr):
    smallest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
    return smallest

arr1 = [2, 5, 1, 3, 0]
arr2 = [8, 10, 5, 7, 9]

print("Smallest element: ", smallest_element(arr1))
print("Smallest element: ", smallest_element(arr2))