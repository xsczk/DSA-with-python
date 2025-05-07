"""A permutation of an array of integers is an arrangement of its members into a sequence
or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr:
[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation
of its integer. More formally, if all the permutations of the array are sorted in one container
according to their lexicographical order, then the next permutation of that array
is the permutation that follows it in the sorted container. If such arrangement is not possible,
the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

- For example, the next permutation of arr = [1,2,3] is [1,3,2].
- Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
- While the next permutation of arr = [3,2,1] is [1,2,3]
because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory."""


class Solution:
    def swap(self, nums: list[int], i: int, j: int) -> None:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    # two pointers
    # Time complexity: O(n)
    def next_permutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 1
        i = n
        # find the first element from the right that satisfy the condition: a[i - 1] < a[i]
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        # check if the current permutation is not the largest one because if i == 0
        # that means the current permutation is in descending order
        # and cannot have next larger permutation
        if i > 0:
            j = n
            while nums[j] <= nums[i - 1]:
                j -= 1
            # swap the element at index i - 1 with the element at index j
            self.swap(nums, i - 1, j)
        # as above: i == 0 means the current permutation cannot have next larger permutation.
        # we reverse these element to the first lowest possible order. It's also true if i != 0
        while i < n:
            self.swap(nums, i, n)
            i += 1
            n -= 1

        print(nums)


solution = Solution()
solution.next_permutation([1, 5, 8, 5, 1, 3, 4, 6, 7])
