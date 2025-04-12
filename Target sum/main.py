"""You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-'
before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1
and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

"""


# Time complexity: O(n * (2 * totalSum + 1))
# Space complexity: O(n * (2 * totalSum + 1))
class Solution:
    def __init__(self):
        self.total_sum = None

    def find_target_sum_ways(self, nums: list[int], target: int) -> int:
        self.total_sum = sum(nums)
        # memo is the array that stores the number of ways to reach the target
        # starting from the current_index with the current_sum
        memo = [
            [float("-inf")] * (2 * self.total_sum + 1) for _ in range(len(nums))
        ]
        return self.calculate_ways(nums, current_index=0, current_sum=0, target=target, memo=memo)

    def calculate_ways(
            self,
            nums: list[int],
            current_index: int,
            current_sum: int,
            target: int,
            memo: list[list[int]],
    ) -> int:
        if current_index == len(nums):
            # Check if the current sum matches the target
            return 1 if current_sum == target else 0

        # Check if the result is already computed
        if memo[current_index][current_sum + self.total_sum] != float('-inf'):
            return memo[current_index][current_sum + self.total_sum]

        # Calculate ways by adding the current number
        add = self.calculate_ways(
            nums,
            current_index + 1,
            current_sum + nums[current_index],
            target,
            memo,
        )

        # Calculate ways by subtracting the current number
        subtract = self.calculate_ways(
            nums,
            current_index + 1,
            current_sum - nums[current_index],
            target,
            memo,
        )

        # Store the result in memoization table
        memo[current_index][current_sum + self.total_sum] = add + subtract

        return memo[current_index][current_sum + self.total_sum]


solution = Solution()
cnt = solution.find_target_sum_ways(nums=[1, 1, 1, 1, 1], target=3)
print(cnt)
