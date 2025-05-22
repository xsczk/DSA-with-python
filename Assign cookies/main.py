"""Assume you are an awesome parent and want to give your children some cookies.
But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie
that the child will be content with; and each cookie j has a size s[j].
If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content.
Your goal is to maximize the number of your content children and output the maximum number."""


class Solution:
    # greedy, two pointers
    # Time complexity: O(m * log m + n * log n) where m is the len of g and n is the len of s
    # Space complexity: O(m + n) for sorting g and s
    def find_content_children(self, g: list[int], s: list[int]) -> int:
        # sort two lists to ensure that each child receives the smallest cookies
        # that meets their greed so that larger cookies can be saved for children with more greed
        g.sort()
        s.sort()
        content_children = 0
        cookie_index = 0
        # make sure there are no leftover cookies
        while content_children < len(g) and cookie_index < len(s):
            if s[cookie_index] >= g[content_children]:
                content_children += 1
            cookie_index += 1
        return content_children
