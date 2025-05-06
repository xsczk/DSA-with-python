"""Given an integer array nums of length n and an integer target,
find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution."""

class Solution:
    def three_sum_closest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = float('inf')
        ans = closest
        for i in range(n - 2):
            # skip duplicate fixed value
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # define two pointers. j is the pointer right after current value,
            # k points to the last element in the array
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(target - s) < closest:
                    # update the closest if absolute difference of target - s
                    # is smaller than the current closest
                    closest = abs(target - s)
                    ans = s
                if target > s:
                    j += 1
                elif target < s:
                    k -= 1
                else:
                    return s
        return ans

solution = Solution()
closest = solution.three_sum_closest([-1,2,1,-4], 1)
print(closest)