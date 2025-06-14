/**
 * Given the root of a binary search tree and an integer k,
 * return true if there exist two elements in the BST such that their sum is equal to k,
 * or false otherwise.
 *
 * Constraints:
 * - The number of nodes in the tree is in the range [1, 104].
 * - -10^4 <= Node.val <= 10^4
 * - root is guaranteed to be a valid binary search tree.
 * - -10^5 <= k <= 10^5
 */

// Definition for a binary tree node.
class TreeNode {
   val: number
   left: TreeNode | null
   right: TreeNode | null

   constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
      this.val = (val === undefined ? 0 : val)
      this.left = (left === undefined ? null : left)
      this.right = (right === undefined ? null : right)
   }
}


function findTarget(root: TreeNode | null, k: number): boolean {
   let ans = false
   const visited = new Set<number>()

   function inorderTraversal(node: TreeNode | null): void {
      if (!node || ans) return
      if (visited.has(node.val)) {
         ans = true
         return
      }
      visited.add(k - node.val)
      inorderTraversal(node.left)
      inorderTraversal(node.right)
   }

   inorderTraversal(root)
   return ans
};