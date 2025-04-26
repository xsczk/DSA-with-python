"""We build a table of n rows (1-indexed). We start by writing 0 in the 1st row.
Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01,
and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

                    0
                  /  \
                0     1
              /  \   / \
            0    1  1   0
k = 3               k
k will be ar the second half of the tree

"""


class Solution:
    # binary tree traversal
    # Time complexity: O(n) -> traverse with n rows
    # Space complexity: O(n) -> recursion call stack
    def kth_grammar(self, n: int, k: int) -> int:
        def dfs_binary(rows: int, kth_node: int, root_val: int) -> int:
            # base case: rows is equal to 1 means that
            # there's only one node -> return its value directly
            if rows == 1:
                return root_val
            # there are 2^(i-1) nodes at i-th row (1-indexed)
            total = 2 ** (rows - 1)
            # if kth_node > total / 2, that means the k-th node will be present
            # in the right half of the last row in our current binary tree and vice versa
            if kth_node > (total / 2):
                # recursively call with right half subtree as an input
                next_root_val = 1 if root_val == 0 else 0
                res = dfs_binary(
                    rows=rows - 1, kth_node=kth_node - (total / 2), root_val=next_root_val
                )
            else:
                next_root_val = 0 if root_val == 0 else 1
                res = dfs_binary(rows=rows - 1, kth_node=kth_node, root_val=next_root_val)
            return res

        return dfs_binary(rows=n, kth_node=k, root_val=0)


solution = Solution()
kth_symbol = solution.kth_grammar(3, 2)
print(kth_symbol)
