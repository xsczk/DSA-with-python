"""Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target
is less than 150 combinations for the given input."""

# Time complexity: O(2^n)
# Space complexity: O(n)
class Solution:
    def combination_sum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []

        def backtrack(cur: list[int], index: int, sum: int) -> None:
            if sum == target:
                # append the copied version of cur to prevent mod
                ans.append(cur[:])
            elif sum < target:
                for i in range(index, len(candidates)):
                    cur_candidate = candidates[i]
                    cur.append(cur_candidate)
                    # index is the same i because a combination can contain an element with
                    # unlimited number of times chosen from candidates
                    backtrack(cur, i, sum + cur_candidate)
                    # pop the last element from cur
                    # if the sum from the most recently callstack
                    # is bigger than the target
                    cur.pop()
            return

        backtrack(cur=[], index=0, sum=0)
        return ans


solution = Solution()
ans = solution.combination_sum(candidates=[2, 3, 6, 7], target=7)
print(ans)
