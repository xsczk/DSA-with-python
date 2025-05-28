/**
 * Given a string s and a string array dictionary, return the longest string in the dictionary
 * that can be formed by deleting some of the given string characters.
 * If there is more than one possible result, return the longest word
 * with the smallest lexicographical order. If there is no possible result,
 * return the empty string.
 *
 * Constraints:
 * - 1 <= s.length <= 1000
 * - 1 <= dictionary.length <= 1000
 * - 1 <= dictionary[i].length <= 1000
 * - s and dictionary[i] consist of lowercase English letters.
 */

// Time complexity: O(n * k) where n is the dictionary length, k is the s length
function findLongestWord(s: string, dictionary: string[]): string {
   /**
    * helper function to check if s is a subsequence of t
    * @param s
    * @param t
    */
   function isSubsequence(s: string, t: string): boolean {
      let j = 0
      for (let i = 0; i < t.length; i++) {
         if (j == s.length) {
            break
         }
         if (t[i] == s[j]) j++
      }
      return j == s.length
   }

   let longest = ''
   for (const word of dictionary) {
      if (isSubsequence(word, s)) {
         // update longest if longer subsequence
         // or subsequence with smaller lexicographical order is found
         if (word.length > longest.length || (word.length == longest.length && word < longest)) {
            longest = word
         }
      }
   }
   return longest
}