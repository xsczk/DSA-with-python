"""Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted,
you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements
in the order they were present in nums initially. The remaining elements of nums
are not important as well as the size of nums.

Return k."""


class Solution:
    # two pointer
    # Time complexity: O(n)
    # Space complexity: O(1) as we modified nums directly, no extra space required
    def remove_duplicates(self, nums: list[int]) -> int:
        # p1 is to track the unique element, p2 to traverse through the array
        p1, p2 = 0, 0
        while p2 < len(nums) - 1:
            p2 += 1
            # if p2 value is equal to p1 value, we update p1 and assign p2 value to p1's position
            if nums[p1] != nums[p2]:
                p1 += 1
                nums[p1] = nums[p2]
        return p1 + 1

    # another approach using two pointer
    # Time and space complexity are the same as first approach
    def remove_duplicates_2(self, nums: list[int]) -> int:
        i = 1
        # since the array is sorted, the first element nums[0] is always unique.
        # therefore, there is no need to compare the first element with any other elements.
        for j in range(1, len(nums)):
            # need to compare j and i - 1 to handle unexpected error happens
            if nums[j] != nums[i - 1]:
                nums[i] = nums[j]
                i += 1

        return i


solution = Solution()
ans = solution.remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
print(ans)
