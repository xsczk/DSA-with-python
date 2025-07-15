/**
 * Given an integer array nums, move all the even integers at the beginning of the array
 * followed by all the odd integers.
 *
 * Return any array that satisfies this condition.
 *
 * Constraints:
 * 1 <= nums.length <= 5000
 * 0 <= nums[i] <= 5000
 */

function sortArrayByParity(nums: number[]): number[] {
   const n = nums.length
   let l = 0, r = n - 1
   while (l < r) {
      while (l < r && nums[l] % 2 == 0) {
         l++
      }
      while (r > l && nums[r] % 2 != 0) {
         r--
      }
      const temp = nums[l]
      nums[l] = nums[r]
      nums[r] = temp
      l++
      r--
   }
   return nums
}