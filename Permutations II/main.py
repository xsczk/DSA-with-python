"""Given a collection of numbers, nums, that might contain duplicates,
return all possible unique permutations in any order.

"""
from collections import Counter


class Solution:
    def permute_unique(self, nums: list[int]) -> list[list[int]]:
        ans = []

        def backtrack_unique(cur: list[int], counter):
            # base case
            if len(cur) == len(nums):
                ans.append(cur[:])
                return
            for x in counter:  # dont pick duplicates
                if counter[x] > 0:
                    cur.append(x)
                    # mark as visited
                    counter[x] -= 1
                    backtrack_unique(cur, counter)
                    cur.pop()
                    # revert as unvisited to continue finding path
                    counter[x] += 1
            return

        backtrack_unique(cur=[], counter=Counter(nums))
        return ans

solution = Solution()
ans = solution.permute_unique([1, 1, 2])
print(ans)
