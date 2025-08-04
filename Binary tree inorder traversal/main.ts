/**
 * Given the root of a binary tree, return the inorder traversal of its nodes' values.
 *
 * Constraints:
 * - The number of nodes in the tree is in the range [0, 100].
 * - -100 <= Node.val <= 100
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

// recursion
function inorderTraversal(root: TreeNode | null): number[] {
   const res: number[] = []

   function helper(node: TreeNode | null): void {
      if (node !== null) {
         // traverse every left subtree nodes
         helper(node.left)
         // append the current parent node's value
         res.push(node.val)
         // traverse the right subtree nodes
         helper(node.right)
      }
   }

   helper(root)
   return res
}

// stack
function inorderTraversalStack(root: TreeNode | null): number[] {
   const res: number[] = []
   const stack: TreeNode[] = []
   let curr = root
   while (curr || stack.length) {
      while (curr) {
         stack.push(curr)
         curr = curr.left
      }
      curr = stack.pop()
      res.push(curr.val)
      curr = curr.right
   }
   return res
}