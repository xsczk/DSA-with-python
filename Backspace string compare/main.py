"""
Given two strings s and t, return true if they are equal when both are typed
into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Constraints:
- 1 <= s.length, t.length <= 200
- s and t only contain lowercase letters and '#' characters.
"""
from itertools import zip_longest
from typing import Iterator


class Solution:
    # simulation
    # time complexity: O(n)
    # space complexity: O(n)
    def back_space_compare(self, s: str, t: str) -> bool:
        def build_string(S: str) -> str:
            ans = []
            for char in S:
                if char != '#':
                    ans.append(char)
                elif ans:
                    ans.pop()
            return ''.join(ans)

        return build_string(s) == build_string(t)

    # generator, scanning from the right
    # time complexity: O(n)
    # space complexity: O(1)
    def back_space_compare_2(self, s: str, t: str) -> bool:
        def generator(S: str) -> Iterator[str]:
            skip = 0
            for char in reversed(S):
                if char == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield char

        return all([x == y for x, y in zip_longest(generator(t), generator(s))])
