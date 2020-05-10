# Find smallest number in rotated sorted array
# 
# Consider an array of sorted integers. Example - [1, 2, 3, 4, 5, 6, 7, 8, 9].
# Now this is rotated by some number k where k < length of array. Example, for
# k = 3, array becomes - [4, 5, 6, 7, 8, 9, 1, 2, 3].
# 
# Given a sorted array which has been rotated by an unknown value, return the
# index of smallest element in the array.
# 
# Example
# 
# Input
# [4, 5, 6, 7, 8, 9, 1, 2, 3]
# 
# Output
# 6
# 
# Write an algorithm to solve this problem and discuss the time complexity. Your
# algorithm must be faster than O(n).

def find_smallest(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] > arr[mid + 1]:
            return mid + 1
        else:
            if arr[mid] > arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

if __name__ == "__main__":
    arr1 = [4, 5, 6, 7, 8, 9, 1, 2, 3]
    arr2 = [2, 1]
    arr3 = [10, 1, 2, 3, 4, 5, 6, 7]
    arr4 = [2, 3, 4, 5, 6, 7, 8, 1]
    testcases = [arr1, arr2, arr3, arr4]

    for t in testcases:
        print('\nInput:', t)
        print('Output:', find_smallest(t))
