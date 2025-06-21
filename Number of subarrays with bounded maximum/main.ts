/**
 * Given an integer array nums and two integers left and right,
 * return the number of contiguous non-empty subarrays such that
 * the value of the maximum array element in that subarray is in the range [left, right].
 *
 * The test cases are generated so that the answer will fit in a 32-bit integer.
 *
 * Constraints:
 * - 1 <= nums.length <= 10^5
 * - 0 <= nums[i] <= 10^9
 * - 0 <= left <= right <= 10^9
 */

// time complexity: O(n)
// space complexity: O(1)
function numSubarrayBoundedMax(nums: number[], left: number,
                               right: number): number {
   function numSubarray(bound: number): number {
      let ans = 0, count = 0
      for (const num of nums) {
         if (num <= bound) {
            count++
         } else {
            count = 0
         }
         ans += count
      }
      return ans
   }

   return numSubarray(right) - numSubarray(left - 1)
};