"""Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

1. arr.length >= 3
2. There exists some i with 0 < i < arr.length - 1 such that:
- arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
- arr[i] > arr[i + 1] > ... > arr[arr.length - 1]"""

# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def valid_mountain_array(self, arr: list[int]) -> bool:
        i = 1
        while i < len(arr) and arr[i] > arr[i-1]:
            i+=1
        if i == 1 or i == len(arr):
            return False
        while i < len(arr) and arr[i] < arr[i-1]:
            i+=1
        return i == len(arr)

solution = Solution()
result = solution.valid_mountain_array([0,1,2,4,3,2,1])
print(result)