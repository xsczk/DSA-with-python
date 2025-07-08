/**
 * You may recall that an array arr is a mountain array if and only if:
 *
 * 1. arr.length >= 3
 * 2. There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
 * - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
 * - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
 *
 * Given an integer array arr, return the length of the longest subarray, which is a mountain.
 * Return 0 if there is no mountain subarray.
 *
 * Constraints:
 * - 1 <= arr.length <= 10^4
 * - 0 <= arr[i] <= 10^4
 */

// two pointers based on the python approach
// time complexity: O(n)
// space complexity: O(1) since variables used inside function are not based on any inputs
function longestMountain(arr: number[]): number {
   const n = arr.length
   let ans = 0, start = 0
   while (start < n) {
      let end = start
      while (end + 1 < n && arr[end] < arr[end + 1]) {
         end++
      }
      // found a peak
      if (end > start) {
         const peak = end
         // find the right boundary of the mountain
         while (end + 1 < n && arr[end] > arr[end + 1]) {
            end++
         }
         if (end > peak) {
            ans = Math.max(ans, end - start + 1)
         }
         // start finding new valid mountain
         start = end
      } else {
         start = end + 1
      }
   }
   return ans
};