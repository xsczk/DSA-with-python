/**
 * You are given two integer arrays nums1 and nums2 both of the same length.
 * The advantage of nums1 with respect to nums2 is the number of indices i
 * for which nums1[i] > nums2[i].
 *
 * Return any permutation of nums1 that maximizes its advantage with respect to nums2.
 *
 * Constraints:
 * - 1 <= nums1.length <= 10^5
 * - nums2.length == nums1.length
 * - 0 <= nums1[i], nums2[i] <= 10^9
 */

// greedy, use original position of nums2 to maintain the order of the answer
function advantageCount(nums1: number[], nums2: number[]): number[] {
   nums1.sort((a, b) => a - b)
   const sortedNums2ByIndices = Array.from({length: nums2.length}, (_, i) => i)
       .sort((a, b) => nums2[a] - nums2[b])
   const res = []
   const remaining = []
   let j = 0
   for (let i = 0; i < nums1.length; i++) {
      if (nums1[i] > nums2[sortedNums2ByIndices[j]]) {
         res[sortedNums2ByIndices[j]] = nums1[i]
         j++
      } else {
         remaining.push(nums1[i])
      }
   }
   for (let i = 0; i < res.length; i++) {
      // detect empty (hole index) value: [0, 1, , 3]
      if (!(i in res)) {
         res[i] = remaining.pop()
      }
   }
   return res
}

// using hashtable
function advantageCount2(nums1: number[], nums2: number[]): number[] {
   const n = nums1.length
   nums1.sort((a, b) => a - b)
   const sortedNums2 = [...nums2].sort((a, b) => a - b)
   const assigned = nums2.reduce((acc, value) => {
      acc[value] = []
      return acc
   }, {})
   const remaining = []
   let j = 0
   for (const num of nums1) {
      if (num > sortedNums2[j]) {
         assigned[sortedNums2[j]].push(num)
         j++
      } else {
         remaining.push(num)
      }
   }
   return nums2.map(v => !_.isEmpty(assigned[v]) ? assigned[v].pop() : remaining.pop())
}

// expected answer: [24, 32, 8, 12]
console.log(advantageCount([12, 24, 8, 32], [13, 25, 32, 11]))