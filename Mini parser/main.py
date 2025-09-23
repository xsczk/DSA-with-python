"""
Given a string s represents the serialization of a nested list, implement a parser
to deserialize it and return the deserialized NestedInteger.

Each element is either an integer or a list whose elements may also be integers or other lists.

Example:
- Input: s = "[123,[456,[789]]]"
- Output: [123,[456,[789]]]
Explanation: Return a NestedInteger object containing a nested list with 2 elements:
1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789

Constraints:
- 1 <= s.length <= 5 * 104
- s consists of digits, square brackets "[]", negative sign '-', and commas ','.
- s is the serialization of valid NestedInteger.
- All the values in the input are in the range [-10^6, 10^6].
"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise, initializes a single integer equal to value.
        """

    def is_integer(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def set_integer(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def get_integer(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def get_list(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if not s.startswith('['):
            return NestedInteger(int(s))
        root = NestedInteger()
        stack = [root]
        i = 0
        while i < len(s):
            if s[i] == ',':
                i += 1
                continue
            elif s[i] == '[':
                new_list = NestedInteger()
                stack[-1].add(new_list)
                # the newList element becomes the current NestedInteger we are working on
                stack.append(new_list)
            elif s[i] == ']':
                stack.pop()
            else:
                j = i
                # we can guarantee s[j] is now only a digit or negative sign '-'
                while j < len(s) and (s[j] == '-' or s[j].isdigit()):
                    j += 1
                integer = int(s[i:j])
                stack[-1].add(NestedInteger(integer))
                i = j
                continue
            i += 1
        return stack[0].get_list()[0]
