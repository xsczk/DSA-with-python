"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Constraints:
- -2^31 <= val <= 2^31 - 1
- Methods pop, top and getMin operations will always be called on non-empty stacks.
- At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""


# design, stack
# time complexity: O(1) for each method
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        cur_min = self.get_min()
        if cur_min is None or val < cur_min:
            cur_min = val
        # consider each node in the stack having a minimum value
        self.stack.append([val, cur_min])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def get_min(self) -> int:
        return self.stack[-1][1] if self.stack else None
