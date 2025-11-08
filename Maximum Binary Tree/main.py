"""
You are given an integer array nums with no duplicates.
A maximum binary tree can be built recursively from nums using the following algorithm:

- Create a root node whose value is the maximum value in nums.
- Recursively build the left subtree on the subarray prefix to the left of the maximum value.
- Recursively build the right subtree on the subarray suffix to the right of the maximum value.
Return the maximum binary tree built from nums.

Example:
- Input: nums = [3,2,1,6,0,5]
- Output: [6,3,5,null,2,0,null,null,1]
Explanation: The recursive calls are as follows:
- The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
    - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
        - Empty array, so no child.
        - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
            - Empty array, so no child.
            - Only one element, so child is a node with value 1.
    - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
        - Only one element, so child is a node with value 0.
        - Empty array, so no child.

Constraints:
- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 1000
- All integers in nums are unique.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursion
    # time complexity: O(n^2) in worst case (sorted nums)
    def construct_maximum_binaryTree(self, nums: list[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        largest = max(nums)
        i = 0
        while i < len(nums):
            if nums[i] == largest:
                break
            i += 1
        return TreeNode(
            val=largest,
            left=self.construct_maximum_binaryTree(nums[:i]),
            right=self.construct_maximum_binaryTree(nums[i + 1:]),
        )

    # monotonic decrease stack
    # time complexity: O(n)
    def construct_maximum_binaryTree2(self, nums: list[int]) -> Optional[TreeNode]:
        max_stack: list[TreeNode] = []
        for num in nums:
            node = TreeNode(val=num)
            while max_stack and max_stack[-1].val < num:
                l_tree = max_stack.pop()
                if not max_stack or max_stack[-1].val > num:
                    # the l_tree will be the left subtree of node because its value < node's value
                    node.left = l_tree
            if max_stack:
                # node will become right subtree of the last pushed tree in max_stack
                max_stack[-1].right = node
            max_stack.append(node)
        # because the stack is kept in decreasing order,
        # the earliest pushed node at the bottom is the global maximum
        # and becomes the tree's root.
        return max_stack[0]
