"""Given an integer array nums, move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array."""

# Time complexity: O(n+m) -> n is the len of the array; m is the number of zero in the array
# Space complexity: O(1)
class Solution:
    def move_zeroes(self, arr: list[int]) -> list[int]:
        zero_index = 0
        for num in arr:
            if num != 0:
                arr[zero_index] = num
                zero_index += 1
        for i in range(zero_index, len(arr)):
            arr[i] = 0
        return arr

    # two pointers, swap elements
    # Time complexity: O(n) - each element is visited once
    # Space complexity: O(1)
    def move_zeroes_2(self, arr: list[int]) -> list[int]:
        p = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                temp = arr[p]
                arr[p] = arr[i]
                arr[i] = temp
                p += 1
        return arr

solution = Solution()
result = solution.move_zeroes_2([0, 1, 2, 0, 12, 0, 3, 10, 0, 0, 25, 40, 0, 35])
print(result)