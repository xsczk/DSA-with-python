"""Find all valid combinations of k numbers that sum up to n
such that the following conditions are true:

- Only numbers 1 through 9 are used.
- Each number is used at most once.
Return a list of all possible valid combinations.
The list must not contain the same combination twice,
and the combinations may be returned in any order.

"""

class Solution:
    def combination_sum_3(self, k:int, n: int) -> list[list[int]]:
        ans = []
        def backtrack(num: int, cur: list[int], sum: int):
            # base case
            if sum == n and len(cur) == k:
                ans.append(cur[:])
                return
            if len(cur) >= n or sum > n: return
            # we are allowed to use only numbers from 1 to 9
            # start from num to skip the number from previous backtrack callstack
            for i in range(num, 10):
                cur.append(i)
                backtrack(num=i + 1, cur=cur, sum=sum+i)
                cur.pop()

        backtrack(num=1, cur=[], sum=0)
        return ans

solution = Solution()
ans = solution.combination_sum_3(k=3, n=9)
print(ans)