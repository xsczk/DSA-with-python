"""
Implement the BSTIterator class that represents an iterator over the in-order traversal
of a binary search tree (BST):

- BSTIterator(TreeNode root) Initializes an object of the BSTIterator class.
The root of the BST is given as part of the constructor. The pointer should be
initialized to a non-existent number smaller than any element in the BST.
- boolean hasNext() Returns true if there exists a number in the traversal
to the right of the pointer, otherwise returns false.
- int next() Moves the pointer to the right, then returns the number at the pointer.

Notice that by initializing the pointer to a non-existent smallest number,
the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be
at least a next number in the in-order traversal when next() is called.

Constraints:
- The number of nodes in the tree is in the range [1, 105].
- 0 <= Node.val <= 10^6
- At most 105 calls will be made to hasNext, and next.
"""
from typing import Optional

"""
Example of a Binary Search Tree:

            7
           / \
          3   15
             /  \
            9    20
The in-order traversal of a Binary Search Tree is: 3 -> 7 -> 9 -> 15 -> 20
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# design, stack
# time complexity: next(): O(n); has_next(): O(1)
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.bst = root
        self.st = []

    def next(self) -> int:
        # traverse over the in-order of the BST
        while self.bst.left:
            self.st.append(self.bst)
            self.bst = self.bst.left
        most_left_node = self.st.pop()
        # save the parent node on the right side for the next method call
        self.bst = most_left_node.right
        return most_left_node.val

    def has_next(self) -> bool:
        return len(self.st) > 0 or self.bst is not None
