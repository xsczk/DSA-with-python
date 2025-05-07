"""Given an array nums with n objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

"""

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def sort_colors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue, n = 0, 0, 0, len(nums)
        # calculating each color count
        for color in nums:
            if color == 0:
                red += 1
            elif color == 1:
                white += 1
            else:
                blue += 1
        # overwrite nums with each color
        for i in range(red):
            nums[i] = 0
        for j in range(white):
            nums[red + j] = 1
        for k in range(blue):
            nums[red + white + k] = 2
