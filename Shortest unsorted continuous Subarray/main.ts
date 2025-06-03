/**
 * Given an integer array nums, you need to find one continuous subarray such that
 * if you only sort this subarray in non-decreasing order, then the whole array
 * will be sorted in non-decreasing order.
 *
 * Return the shortest such subarray and output its length.
 *
 * Constraints:
 * 1 <= nums.length <= 10^4
 * -10^5 <= nums[i] <= 10^5
 */

function findUnsortedSubarray(nums: number[]): number {
   let start = 0,
       end = nums.length - 1
   // find the initial boundaries of the unsorted subarray
   while (start + 1 <= end && nums[start + 1] >= nums[start]) {
      start++
   }
   while (end - 1 >= start && nums[end - 1] <= nums[end]) {
      end--
   }
   // if the array is already sorted
   if (start == end) return 0
   // find the min and max values in the unsorted subarray
   const maxValue = Math.max(...nums.slice(start, end + 1))
   const minValue = Math.min(...nums.slice(start, end + 1))
   // expand the boundaries to include all elements that are out of place
   while (start > 0 && nums[start - 1] > minValue) {
      start--
   }
   while (end < nums.length - 1 && nums[end + 1] < maxValue) {
      end++
   }
   return end - start + 1
}

console.log(findUnsortedSubarray([1, 2, 3, 4, 3, 5, 6, 5, 3, 6, 7, 3, 6, 7, 8]))