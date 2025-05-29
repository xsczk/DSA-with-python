/**
 * Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.
 *
 * A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:
 *
 * - 0 <= i, j < nums.length
 * - i != j
 * - |nums[i] - nums[j]| == k
 * Notice that |val| denotes the absolute value of val.
 *
 * Constraints:
 * - 1 <= nums.length <= 10^4
 * - -10^7 <= nums[i] <= 10^7
 * - 0 <= k <= 10^7
 */

function findPairs(nums: number[], k: number): number {
   const count = new Map<number, number>()
   let res = 0
   for (const num of nums) {
      // equivalent to Counter build-in method in python
      count.set(num, (count.get(num) || 0) + 1)
   }
   count.forEach((freq, num) => {
      if ((k == 0 && freq >= 2) || (k != 0 && count.has(num + k))) {
         res++
      }
   })
   return res
}

console.log(findPairs([3, 1, 4, 1, 5], 2))