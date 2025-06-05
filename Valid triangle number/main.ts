/**
 * Given an integer array nums, return the number of triplets chosen from the array
 * that can make triangles if we take them as side lengths of a triangle.
 *
 * Constraints:
 * - 1 <= nums.length <= 1000
 * - 0 <= nums[i] <= 1000
 */

function triangleNumber(nums: number[]): number {
   nums.sort((a, b) => a - b)
   let ans = 0
   for (let k = 2; k < nums.length; k++) {
      let i = 0, j = k - 1
      while (i < j) {
         if (nums[i] + nums[j] <= nums[k]) {
            i++
         } else {
            ans += j - i
            j--
         }
      }
   }
   return ans
}

console.log(triangleNumber([2, 2, 3, 4]))