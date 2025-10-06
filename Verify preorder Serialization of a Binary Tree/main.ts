/**
 * One way to serialize a binary tree is to use preorder traversal.
 * When we encounter a non-null node, we record the node's value.
 * If it is a null node, we record using a sentinel value such as '#'.
 *
 * Given a string of comma-separated values preorder,
 * return true if it is a correct preorder traversal serialization of a binary tree.
 *
 * It is guaranteed that each comma-separated value in the string
 * must be either an integer or a character '#' representing null pointer.
 *
 * You may assume that the input format is always valid.
 *
 * For example, it could never contain two consecutive commas, such as "1,,3".
 * Note: You are not allowed to reconstruct the tree.
 *
 * Constraints:
 * - 1 <= preorder.length <= 104
 * - preorder consist of integers in the range [0, 100] and '#' separated by commas ','.
 */


function isValidSerialization(preorder: string): boolean {
   const st: string[] = []
   const preorderList = preorder.split(',')
   for (let i = preorderList.length - 1; i >= 0; i -= 1) {
      if (st.length >= 2 &&
          !Number.isNaN(Number(preorderList[i])) &&
          st.at(-1) == "#" && st.at(-1) == st.at(-2)
      ) {
         st.pop()
      } else {
         st.push(preorderList[i])
      }
   }
   return st.length == 1 && st[0] == '#'
};