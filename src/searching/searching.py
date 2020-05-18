def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        print(arr[i])
        if arr[i] == target:
            return i


    return -1   # not found

arr1 = [-2, 7, 3, -9, 5, 1, 0, 4, -6]
print(linear_search(arr1, -6))

# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid    

    return -1  # not found
