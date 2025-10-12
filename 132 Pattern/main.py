"""
Given an array of n integers nums, a 132 pattern is a subsequence
of three integers nums[i], nums[j] and nums[k] such that
i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Example 1:
- Input: nums = [1,2,3,4]
- Output: false
- Explanation: There is no 132 pattern in the sequence.

Example 2:
- Input: nums = [3,1,4,2]
- Output: true
- Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:
- Input: nums = [-1,3,2,0]
- Output: true
- Explanation: There are three 132 patterns in the sequence:
[-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

Constraints:
- n == nums.length
- 1 <= n <= 2 * 10^5
- -10^9 <= nums[i] <= 10^9
"""


class Solution:
    # using monotonic decreasing stack
    def find132pattern(self, nums: list[int]) -> bool:
        """
        we're using decreasing stack and keep track of the best 2 element
        in the 132 pattern. If the current element is smaller than the best 2,
        we know nums's met the expectation.
        """
        best_2 = float('-inf')
        decreasing = []
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < best_2:
                return True
            while decreasing and decreasing[-1] < nums[i]:
                best_2 = decreasing.pop()
            decreasing.append(nums[i])
        return False


solution = Solution()
print(solution.find132pattern(nums=[3, 1, 4, 2]))
