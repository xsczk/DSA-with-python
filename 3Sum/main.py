"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets."""


class Solution:
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        # sort the nums array for easier binary search
        nums.sort()
        n, res = len(nums), []
        for i in range(n):
            # since nums is sorted => if cur > 0, that means
            # there is no element after this that their sum can be 0
            if nums[i] > 0:
                break
            # in current iteration, if cur value == value in previous loop,
            # we skip and move to the next interation to avoid duplicate triplets
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            # define next two pointer as nums[i] is fixed => the problem turns into find pairs problem
            # such that  the sum of the pair equals to -nums[i]
            j, k = i + 1, n - 1
            # binary search section
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    # skip duplicate if nums[j] == nums[j-1]. Same as above
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return res


solution = Solution()
triplets = solution.three_sum([-1, 0, 1, 2, -1, -4])
print(triplets)
