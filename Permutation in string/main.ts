/**
 * Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
 *
 * In other words, return true if one of s1's permutations is the substring of s2.
 *
 * Constraints:
 * - 1 <= s1.length, s2.length <= 10^4
 * - s1 and s2 consist of lowercase English letters.
 */

// sliding window, hash table
// Time complexity: O(s2.length)
// Space complexity: O(1) - two array with fixed size of 26
function checkInclusion(s1: string, s2: string): boolean {
   if (s1.length > s2.length) {
      return false
   }
   // there are 26 alphabet letters
   const s1Count = new Array(26).fill(0)
   const windowCount = [...s1Count]
   // count the characters frequency represent in s1 and the first window
   for (let i = 0; i < s1.length; i++) {
      s1Count[s1.charCodeAt(i) - 'a'.charCodeAt(0)] += 1
      windowCount[s2.charCodeAt(i) - 'a'.charCodeAt(0)] += 1
   }

   /**
    * check if two array is equal in value
    */
   function isEqual(a: number[], b: number[]) {
      for (let i = 0; i < 26; i++) {
         if (a[i] != b[i]) return false
      }
      return true
   }

   if (isEqual(s1Count, windowCount)) {
      return true
   }
   // sliding the window through s2
   for (let i = s1.length; i < s2.length; i++) {
      // remove left most character count by 1
      windowCount[s2.charCodeAt(i - s1.length) - 'a'.charCodeAt(0)] -= 1
      // add new character at right most for each check
      windowCount[s2.charCodeAt(i) - 'a'.charCodeAt(0)] += 1
      if (isEqual(s1Count, windowCount)) {
         return true
      }
   }
   return false
}

console.log(checkInclusion('ab', 'eidbaooo'))