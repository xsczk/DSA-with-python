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

solution = Solution()
result = solution.move_zeroes([0, 1, 2, 0, 12, 0, 3, 10, 0, 0, 25, 40, 0, 35])
print(result)