"""Given an integer array nums of unique elements,
return all possible subsets (the power set).

The solution set must not contain duplicate subsets.
Return the solution in any order."""

# example: [1,2]
"""
ans: [[], [1], [1,2], [2]]
          curr
     
        []
        /\
    [1]     [2]
    /
[1,2]

"""


# backtracking
# Time complexity:
# Space complexity:
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        cur = []
        self.backtracking(ans=ans, nums=nums, cur=cur, index=0)
        return ans

    def backtracking(self, ans: list[list[int]], nums: list[int], cur: list[int], index: int) -> None:
        # append the copy of cur to prevent the modification in these below code
        ans.append(cur[:])
        for i in range(index, len(nums)):
            num = nums[i]
            if num not in cur:
                cur.append(num)
                # continue recursive with index up to 1
                self.backtracking(ans=ans, nums=nums, cur=cur, index=i + 1)
                # back the current to previous state to continue the backtracking
                cur.pop()
        return


solution = Solution()
ans = solution.subsets(nums=[1, 2, 3])
print(ans)
