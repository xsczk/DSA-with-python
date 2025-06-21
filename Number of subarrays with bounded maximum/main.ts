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
}

// expand the valid window
// time complexity: O(n)
// space complexity: O(1)
function numSubarrayBoundedMax2(nums: number[], left: number,
                                right: number): number {
   let x = -1, y = -1, ans = 0
   for (let i = 0; i < nums.length; i++) {
      const num = nums[i]
      // expand the valid subarray
      if (num >= left) y = i
      // reset and start new window subarray as num is not in valid boundary
      if (num > right) x = i
      // with each loop, re-calculate ans
      ans += y - x
   }
   return ans
}

numSubarrayBoundedMax2([2, 1, 4, 3], 2, 3)