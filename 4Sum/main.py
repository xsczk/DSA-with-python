"""Given an array nums of n integers, return an array of all the unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that:

- 0 <= a, b, c, d < n
- a, b, c, and d are distinct.
- nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Constraints:
- 1 <= nums.length <= 200
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
"""


class Solution:
    # naive approach with two pointers to reduce complexity
    # Time complexity: O(n^3)
    # Space complexity: O(1)
    def four_sum(self, nums: list[int], target: int) -> list[list[int]]:
        # -2,-1,0,0,1,2
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n - 3):
            # if sum of first 4 nums greater than target, break the loop
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            #  skip duplicate cases
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # turns problem into 3sum sub problem
            for j in range(i + 1, n - 2):
                # break nested loop if sum of these nums greater than target
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                # continue the nested loop if nums[j] is not big enough
                if nums[i] + nums[j] + nums[-1] + nums[-2] < target:
                    continue
                # skip duplicate cases
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l, r = j + 1, n - 1
                # binary search section
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s > target:
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        # skip duplicate cases
                        while l + 1 < r and nums[l + 1] == nums[l]:
                            l += 1
                        while r - 1 > l and nums[r - 1] == nums[r]:
                            r -= 1
                        l += 1
                        r -= 1
        return ans


solution = Solution()
quadruplets = solution.four_sum(nums=[-2, -1, -1, 1, 1, 2, 2], target=0)
print(quadruplets)
