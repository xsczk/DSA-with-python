/**
 * Sometimes people repeat letters to represent extra feeling. For example:
 *
 * - "hello" -> "heeellooo"
 * - "hi" -> "hiiii"
 * In these strings like "heeellooo", we have groups of adjacent letters
 * that are all the same: "h", "eee", "ll", "ooo".
 *
 * You are given a string s and an array of query strings words.
 * A query word is stretchy if it can be made to be equal to s
 * by any number of applications of the following extension operation:
 * choose a group consisting of characters c, and add some number of characters c
 * to the group so that the size of the group is three or more.
 *
 * For example, starting with "hello", we could do an extension on the group "o"
 * to get "hellooo", but we cannot get "helloo" since the group "oo" has a size less than three.
 * Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".
 * If s = "helllllooo", then the query word "hello" would be stretchy
 * because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.
 *
 * Return the number of query strings that are stretchy.
 *
 * Constraints:
 * - 1 <= s.length, words.length <= 100
 * - 1 <= words[i].length <= 100
 * - s and words[i] consist of lowercase letters.
 */
import {isEqual} from 'lodash'

// based on the python approach: Run Length Encoding
function expressiveWords(s: string, words: string[]): number {
   function RLE(S: string): [string[], number[]] {
      const arr = S.split('')
      let j = 0
      const res = arr.reduce((cur, c, i) => {
         const {group, count} = cur
         if (i != 0 && c != S[i - 1]) {
            group.push(S[i - 1])
            count.push(i - j)
            j = i
         }
         if (i == S.length - 1) {
            group.push(c)
            count.push(i - j + 1)
         }
         return cur
      }, {group: [] as string[], count: [] as number[]})
      return [res.group, res.count]
   }

   const [R, count] = RLE(s)
   let ans = 0
   for (const word of words) {
      const [R2, count2] = RLE(word)
      if (!isEqual(R, R2)) continue
      ans += +count.every((v,
                           i) => v >= Math.max(count2[i], 3) || v == count2[i])
   }
   return ans
}

console.log(expressiveWords("heeellooo", ["hello", "hi", "helo"]))