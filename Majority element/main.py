"""Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array."""


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def majority_element(self, nums: list[int]) -> int:
        m = {}
        for num in nums:
            m[num] = m.get(num, 0) + 1
            if m[num] > len(nums) // 2:
                return num

    def optimal_majority_element(self, nums: list[int]) -> int:
        majority = nums[0]
        count = 1
        n = len(nums)
        for i in range(1, n):
            curr = nums[i]
            if count == 0:
                majority = curr
            if majority == curr:
                count += 1
            else:
                count -= 1
        return majority


solution = Solution()
result = solution.optimal_majority_element(nums=[2, 2, 1, 1, 1, 2, 2])
print(result)
