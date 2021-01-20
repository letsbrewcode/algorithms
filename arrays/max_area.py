# Max Area
# Given an array arr, each item arr[i] in array represents a vertical line of
# length a[i]. You have to find the maximum area that can be formed by choosing
# two vertical lines in the array.

# Example:
# arr = [1,8,6,2,5,4,8,3,7]
#
#                |              |
#                |              |     |
#                |  |           |     |
#                |  |     |     |     |
#                |  |     |  |  |     |
#                |  |     |  |  |  |  |
#                |  |  |  |  |  |  |  |
#             |  |  |  |  |  |  |  |  |
#             -- -- -- -- -- -- -- -- --
# Values:     1  8  6  2  5  4  8  3  7
# Indices:    0  1  2  3  4  5  6  7  8
#
# Output: 49
# Explanation: The maximum area comes from choosing indices, 1 and 8
# width  = 8 - 1 = 7
# height = 7 (Minimum of 7 and 8)
# Area = 7 x 7 = 49 sq units

def brute_force(nums):
    result = 0
    L = len(nums)
    
    for x in range(L):
        for y in range(x + 1, L):
            height = min(nums[x], nums[y])
            width = y - x
            area = height * width
            
            result = max(result, area)
    
    return result

def two_pointer(nums):
    L = len(nums)
    result = 0
    
    x = 0
    y = L - 1
    
    while y > x:
        height = min(nums[x], nums[y])
        width = y - x
        area = height * width
        
        result = max(result, area)
        
        if nums[x] < nums[y]:
            x += 1
        else:
            y -= 1
    
    return result
        

if __name__ == "__main__":
    arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(brute_force(arr))
    print(two_pointer(arr))
