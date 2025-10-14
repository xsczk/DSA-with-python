"""
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1]
is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order
next in the array, which means you could search circularly to find its next greater number.
If it doesn't exist, return -1 for this number.

Example 1:
- Input: nums = [1,2,1]
- Output: [2,-1,2]
- Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number.
The second 1's next greater number needs to search circularly, which is also 2.

Example 2:
- Input: nums = [1,2,3,4,3]
- Output: [2,3,4,-1,4]

Constraints:
- 1 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
"""


class Solution:
    # monotonic decreasing stack
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        # instead of storing nums value, we store the indices
        # since there could be duplicates in the nums
        dec_st = []
        res = [-1] * len(nums)
        for i in range(2 * len(nums) - 1, -1, -1):
            while dec_st and nums[dec_st[-1]] <= nums[i % len(nums)]:
                dec_st.pop()
            # if dec_st is not empty, assign the value of res at related indices be
            # the value of nums at the indices which is the top of dec_st
            if dec_st:
                res[i % len(nums)] = nums[dec_st[-1]]
            dec_st.append(i % len(nums))
        return res


solution = Solution()
print(solution.nextGreaterElements([1, 2, 7, 4, 3, 5]))
