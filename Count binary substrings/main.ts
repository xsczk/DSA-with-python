/**
 * Given a binary string s, return the number of non-empty substrings
 * that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings
 * are grouped consecutively.
 *
 * Substrings that occur multiple times are counted the number of times they occur.
 *
 * Constraints:
 * - 1 <= s.length <= 10^5
 * - s[i] is either '0' or '1'.
 */

// group by character
// time complexity: O(n)
// space complexity: O(n)
function countBinarySubstrings(s: string): number {
   const group = [1]
   // build a list of group
   for (let i = 1; i < s.length; i++) {
      if (s[i - 1] != s[i]) {
         group.push(1)
      } else {
         group[group.length - 1] += 1
      }
   }
   let ans = 0
   for (let i = 1; i < group.length; i++) {
      ans += Math.min(group[i], group[i - 1])
   }
   return ans
}

// linear scan based on above approach without using group list
// time complexity: O(n)
// space complexity: O(1)
function countBinarySubstrings2(s: string): number {
   let ans = 0, prev = 0, cur = 1
   for (let i = 1; i < s.length; i++) {
      if (s[i - 1] != s[i]) {
         ans += Math.min(prev, cur)
         prev = cur
         cur = 1
      } else {
         cur += 1
      }
   }
   return ans + Math.min(prev, cur)
}