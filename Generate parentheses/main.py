"""Given n pairs of parentheses, write a function
to generate all combinations of well-formed parentheses."""

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        # increase number of open parentheses until n at first,
        # then increase number of close parentheses until n
        def dfs(open: int, close: int, s: str) -> None:
            if open == close and open + close == n * 2:
                res.append(s)
                return
            if open < n:
                dfs(open + 1, close, s + "(")
            if close < open:
                dfs(open, close + 1, s + ")")

        dfs(open=0, close=0, s="")

        return res


solution = Solution()
ans = solution.generateParenthesis(2)
print(ans)
