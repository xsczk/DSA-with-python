/**
 * Given the root of a binary tree, flatten the tree into a "linked list":
 *
 * - The "linked list" should use the same TreeNode class
 * where the right child pointer points to the next node in the list
 * and the left child pointer is always null.
 * - The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 *
 * Constraints:
 * - The number of nodes in the tree is in the range [0, 2000].
 * - -100 <= Node.val <= 100
 */

/**
 *                 1
 *               /   \
 *              2     5     =>  1 -> 2 -> 3 -> 4 -> 5 -> 6
 *             / \     \
 *            3   4     6
 */

// Definition for a binary tree node.
class TreeNode {
   val: number;
   left: TreeNode | null;
   right: TreeNode | null;

   constructor(val = 0, left = null, right = null) {
      this.val = val
      this.left = left
      this.right = right
   }
}

function preOrderTraversal(stack: (TreeNode | undefined)[],
                           node?: TreeNode): void {
   if (node) {
      preOrderTraversal(stack, node.right)
      preOrderTraversal(stack, node.left)
      stack.push(node)
   }
}


/**
 * Do not return anything, modify root in-place instead.
 */
function flatten(root: TreeNode | null) {
   const stack: Parameters<typeof preOrderTraversal>[0] = []
   if (root) {
      preOrderTraversal(stack, root)
   }
   while (stack.length) {
      const head = stack.pop()
      head.left = null
      if (stack.length) {
         head.right = stack[stack.length - 1]
      } else {
         head.right = null
      }
   }
}

class Solution {
   head: TreeNode | null;

   constructor() {
      this.head = null;
   }

   preOrderHelper(node: TreeNode | null) {
      if (node) {
         this.preOrderHelper(node.right)
         this.preOrderHelper(node.left)
         node.left = null
         node.right = this.head
         this.head = node
      }
   }

   flatten(root: TreeNode | null) {
      this.preOrderHelper(root)
   }
}