"""
There are n dominoes in a line, and we place each domino vertically upright.
In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left.
Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides,
it stays still due to the balance of the forces. (*)

For the purposes of this question, we will consider that
a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

- dominoes[i] = 'L', if the ith domino has been pushed to the left,
- dominoes[i] = 'R', if the ith domino has been pushed to the right, and
- dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.

Constraints:
- n == dominoes.length
- 1 <= n <= 10^5
- dominoes[i] is either 'L', 'R', or '.'.
"""


class Solution:
    # time complexity: O(n)
    # space complexity: O(n)
    def push_dominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        symbols = [(i, x) for i, x in enumerate(dominoes) if x != '.']
        # handle the edge cases. ex: R...
        symbols = [(-1, 'L')] + symbols + [(n, 'R')]
        ans = list(dominoes)
        for symbol_info in range(1, len(symbols)):
            i, x = symbols[symbol_info - 1]
            j, y = symbols[symbol_info]
            # R...R or L...L => replace "." with R or L
            if x == y:
                for k in range(i + 1, j):
                    ans[k] = x
            # R...L
            elif x == 'R' and y == 'L':
                l, r = i + 1, j - 1
                while l < r:
                    ans[l] = x
                    ans[r] = y
                    l, r = l + 1, r - 1
            # L...R: we do not need to do anything further since (*) is satisfied
        return ''.join(ans)

    # concise version
    def push_dominoes_2(self, dominoes: str) -> str:
        symbols = [(i, x) for i, x in enumerate(dominoes) if x != '.']
        # handle the edge cases. ex: R...
        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]
        ans = list(dominoes)
        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            if x == y:
                for k in range(i + 1, j):
                    ans[k] = x
            # x = R and y = L
            elif x > y:
                l, r = i + 1, j - 1
                while l < r:
                    ans[l] = x
                    ans[r] = y
                    l, r = l + 1, r - 1
        return ''.join(ans)


solution = Solution()
print(solution.push_dominoes_2(".L.R...LR..L.."))
