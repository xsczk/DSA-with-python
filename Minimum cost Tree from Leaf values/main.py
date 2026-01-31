"""
Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal
of the tree.
The value of each non-leaf node is equal to the product of the largest leaf value
in its left and right subtree, respectively.
Among all possible binary trees considered, return the smallest possible sum
of the values of each non-leaf node. It is guaranteed this sum fits into a 32-bit integer.

A node is a leaf if and only if it has zero children.

Constraints:
- 2 <= arr.length <= 40
- 1 <= arr[i] <= 15
- It is guaranteed that the answer fits into a 32-bit signed integer
(i.e., it is less than 2^31).
"""


class Solution:
    # arr = [8,4,1,2,5]
    # tree inorder traversal: [8, 40, 4, 8, 1, 2, 2, 20, 5]
    # expectation: 70 = 2 + 8 + 20 + 40
    """
          40
          / \
         8  20
            / \
           8   5
          / \
         4   2
            / \
           1   2
    """

    # greedy
    def mct_from_leaf_values(self, arr: list[int]) -> int:
        res = 0
        while len(arr) > 1:
            i = arr.index(min(arr))
            res += min(arr[i - 1:i] + arr[i + 1:i + 2]) * arr.pop(i)
        return res
