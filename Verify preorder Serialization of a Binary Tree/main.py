"""
One way to serialize a binary tree is to use preorder traversal.
When we encounter a non-null node, we record the node's value.
If it is a null node, we record using a sentinel value such as '#'.

Given a string of comma-separated values preorder,
return true if it is a correct preorder traversal serialization of a binary tree.

It is guaranteed that each comma-separated value in the string
must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid.

For example, it could never contain two consecutive commas, such as "1,,3".
Note: You are not allowed to reconstruct the tree.

Constraints:
- 1 <= preorder.length <= 104
- preorder consist of integers in the range [0, 100] and '#' separated by commas ','.
"""


class Solution:
    # valid parent and two children can be turned into one #
    def is_valid_serialization(self, preorder: str) -> bool:
        st = []
        preorder = preorder.split(',')
        for i in range(len(preorder) - 1, -1, -1):
            if (len(st) >= 2
                    and preorder[i].isdigit()
                    and st[-1] == st[-2] == '#'):
                st.pop()
            else:
                st.append(preorder[i])
        return len(st) == 1 and st[0] == '#'
