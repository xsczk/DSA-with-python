/**
 * You are given a string s. We want to partition the string into as many parts as possible
 * so that each letter appears in at most one part. For example, the string "ababcc" can be
 * partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"]
 * are invalid.
 *
 * Note that the partition is done so that after concatenating all the parts in order,
 * the resultant string should be s.
 *
 * Return a list of integers representing the size of these parts.
 *
 * Constraints:
 * - 1 <= s.length <= 500
 * - s consists of lowercase English letters.
 */

function partitionLabels(s: string): number[] {
   const lastOccurrence = Array.from({length: 26}, () => 0)
   const n = s.length
   // find the last index of each character's occurrence in the s
   for (let i = 0; i < n; i++) {
      lastOccurrence[s[i].charCodeAt(0) - 'a'.charCodeAt(0)] = i
   }
   // start & end to track the start and end points of the current partition
   let start = 0, end = 0
   const ans = []
   for (let i = 0; i < n; i++) {
      const lastIndex = lastOccurrence[s[i].charCodeAt(0) - 'a'.charCodeAt(0)]
      // update the end pointer aka the boundary of the current partition
      end = Math.max(end, lastIndex)
      if (i == end) {
         ans.push(end - start + 1)
         start = end + 1
      }
   }
   return ans
}

console.log(partitionLabels("ababcbacadefegdehijhklij"))