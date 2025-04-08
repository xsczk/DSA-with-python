"""Given an integer array nums, return all the different possible non-decreasing subsequences
of the given array with at least two elements. You may return the answer in any order."""

class Solution:
    def find_subsequences(self, nums: list[int]) -> list[list[int]]:
        # using set DS to remove duplicate items in ans
        ans = set()
        def backtrack(cur: list[int], index: int):
            # only add to ans if cur contains two or more elements
            if len(cur) >= 2:
                ans.add(tuple(cur))
            # base case
            if index == len(nums): return
            for i in range(index, len(nums)):
                # only append to cur if last cur element is equal or smaller than nums[i]
                if not cur or cur[-1] <= nums[i]:
                    # change
                    cur.append(nums[i])
                    # recursive
                    backtrack(cur, i + 1)
                    # backtrack to continue other paths
                    cur.pop()
        backtrack(cur=[], index=0)
        return list(ans)

solution = Solution()
ans = solution.find_subsequences([4,6,7,7])
print(ans)