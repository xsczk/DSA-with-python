"""Given a string s, you can transform every letter individually to be
lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

"""

# depth-first-search
class Solution:
    def letter_case_permutation(self, s: str) -> list[str]:
        ans = []
        def backtrack(i: int, cur: str):
            if i == len(s):
                ans.append(cur)
                return
            # if element is a alphabet letter
            if s[i].isalpha():
                # turn lower to upper and vice versa
                backtrack(i+1, cur + s[i].swapcase())
            backtrack(i+1, cur + s[i])
        backtrack(0, '')
        return ans

solution = Solution()
ans = solution.letter_case_permutation('a1b2')
print(ans)