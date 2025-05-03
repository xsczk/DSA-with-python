"""Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

"""

class Solution:
    # two pointer
    # Time complexity: O(n)
    # Space complexity: O(n) we define ans which has length equal to len nums
    def sorted_square(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n
        l, r = 0, n - 1
        # in this case, right number will produce bigger square since the init nums is sorted.
        # so we traverse the nums in reverse order and put the bigger value at the index from right to left.
        for i in range(n - 1, -1, -1):
            # we just only care about the abs of its value
            if abs(nums[l]) < abs(nums[r]):
                ans[i] = nums[r] * nums[r]
                r -= 1
            else:
                ans[i] = nums[l] * nums[l]
                l += 1
        return ans


solution = Solution()
ans = solution.sorted_square([-4,-1,0,3,10])
print(ans)