"""Given an integer array nums, rotate the array to the right by k steps,
where k is non-negative."""


class Solution:
    # using additional space
    # Time complexity: O(n)
    # Space complexity: O(n)
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # reduce unnecessary rotate count if k > n
        k %= n
        ans = nums[-k:] + nums[:-k]
        for i in range(n):
            nums[i] = ans[i]

    # two pointers, reverse the original list
    # Time complexity: O(n)
    # Space complexity: O(1)
    def rotate_2(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # reduce unnecessary rotate count if k > n
        k %= n

        def reverse(i: int, j: int):
            while i < j:
                # swap two element
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
                j -= 1

        # we reverse three times to retrieve the result
        # reverse entire original list: [1, 2, 3, 4, 5, 6, 7] -> [7, 6, 5, 4, 3, 2, 1]
        reverse(i=0, j=n - 1)
        # reverse the first k elements: [7, 6, 5, 4, 3, 2, 1] -> [5, 6, 7, 4, 3, 2, 1]
        reverse(i=0, j=k - 1)
        # reverse remaining elements after the k elements: [5, 6, 7, 4, 3, 2, 1] -> [5, 6, 7, 1, 2, 3, 4]
        reverse(i=k, j=n - 1)
        print(nums)


solution = Solution()
solution.rotate_2([1, 2, 3, 4, 5, 6, 7], 3)
