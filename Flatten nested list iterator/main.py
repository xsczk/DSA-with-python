"""
You are given a nested list of integers nestedList. Each element is either an integer
or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

- NestedIterator(List<NestedInteger> nestedList) Initializes the iterator
with the nested list nestedList.
- int next() Returns the next integer in the nested list.
- boolean hasNext() Returns true if there are still some integers in the nested list
and false otherwise.

Your code will be tested with the following pseudocode:

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res

- If res matches the expected flattened list, then your code will be judged as correct.

Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements
returned by next should be: [1,4,6].

Constraints:
- 1 <= nestedList.length <= 500
- The values of the integers in the nested list is in the range [-106, 106].
"""

# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
class NestedInteger:
    def is_integer(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        pass

    def get_integer(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        pass

    def get_list(self) -> list[NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        pass

class NestedIterator:
    def __init__(self, nested_list: list[NestedInteger]):
        self.stack: list[NestedInteger] = []
        # reverse the order of the nestedList and push to the stack
        for i in range(len(nested_list) - 1, -1, -1):
            self.stack.append(nested_list[i])

    # time complexity: O(1)
    def next(self) -> int:
        # remove the recent integer in the stack
        return self.stack.pop().get_integer()

    def has_next(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            # return true if we found an integer
            if top.is_integer():
                return True
            nested_list = self.stack.pop().get_list()
            # reverse the order of the element in nested list and push to the stack again
            # [1, [4, [6]]] -> [[4, [6]], 1] -> [[6], 4, 1] -> [6, 4, 1]
            # the next method we can only just pop from the stack until it's empty
            for i in range(len(nested_list) - 1, -1, -1):
                self.stack.append(nested_list[i])
        return False

