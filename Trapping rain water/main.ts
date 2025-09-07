/**
 * Given n non-negative integers representing an elevation map where the width of each bar is 1,
 * compute how much water it can trap after raining.
 *
 * Example: (see the rainwatertrap image for more details)
 * - Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
 * - Output: 6
 * - Explanation: The above elevation map (black section) is represented
 * by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water
 * (blue section) are being trapped.
 *
 * Constraints:
 * - n == height.length
 * - 1 <= n <= 2 * 10^4
 * - 0 <= height[i] <= 10^5
 */

function trap(height: number[]): number {
   let water = 0, l = 0, r = height.length - 1;
   let left_max = height[l], right_max = height[r]
   while (l < r) {
      if (left_max < right_max) {
         l++
         const current_height = height[l]
         left_max = Math.max(left_max, current_height)
         water += left_max - current_height
      } else {
         r--
         const current_height = height[r]
         right_max = Math.max(right_max, current_height)
         water += right_max - current_height
      }
   }
   return water
}