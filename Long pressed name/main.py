"""
Your friend is typing his name into a keyboard. Sometimes, when typing a character c,
the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that
it was your friends name, with some characters (possibly none) being long pressed.

Constraints:
- 1 <= name.length, typed.length <= 1000
- name and typed consist of only lowercase English letters.
"""
from itertools import groupby


class Solution:
    # two pointers
    # time complexity: O(n)
    # space complexity: O(1)
    def is_long_pressed_name(self, name: str, typed: str) -> bool:
        np, tp = 0, 0
        # advance two pointers, until we exhaust one of the strings
        while np < len(name) and tp < len(typed):
            # if there's a match, move both pointers forward
            if name[np] == typed[tp]:
                np += 1
                tp += 1
            # if there's a mismatch but the current typed is similar to its the previous, we can skip
            elif tp >= 1 and typed[tp] == typed[tp - 1]:
                tp += 1
            else:
                return False
        # if there's still some characters left *unmatched* in the origin string,
        # then we don't have a match.
        # e.g.  name = "alexd"  typed = "ale"
        if np != len(name):
            return False
        # in the case that there're some redundant characters left in typed
        # we could still have a match.
        # e.g.  name = "abc"  typed = "abccccc"
        while tp < len(typed):
            if typed[tp] != typed[tp - 1]:
                return False
            tp += 1
        return True

    # concise version using groupby and zip
    def is_long_pressed_name_2(self, name: str, typed: str) -> bool:
        def groupByChar(s: str) -> list[tuple[str, int]]:
            """
            group each character with the number of times it appears.
            """
            return [(c, len(list(gr))) for c, gr in groupby(s)]

        name_group = groupByChar(name)
        typed_group = groupByChar(typed)

        if len(name_group) != len(typed_group):
            return False
        return all([k1 == k2 and v1 <= v2 for (k1, v1), (k2, v2) in
                    zip(name_group, typed_group)])
