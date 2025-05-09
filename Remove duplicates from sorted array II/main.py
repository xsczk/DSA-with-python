"""Given an integer array nums sorted in non-decreasing order,
remove some duplicates in-place such that each unique element appears at most twice.
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages,
you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates,
then the first k elements of nums should hold the final result.
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array.
You must do this by modifying the input array in-place with O(1) extra memory.

constrains:
- 1 <= nums.length <= 3 * 104
- -10^4 <= nums[i] <= 10^4
- nums is sorted in non-decreasing order.

"""


class Solution:
    def remove_duplicates(self, nums: list[int]) -> int:
        k = 2
        # since the output nums will have each unique element appears at most twice
        # we don't care the first two number
        for i in range(2, len(nums)):
            # update nums[k] if current element is different
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
        return k


solution = Solution()
ans = solution.remove_duplicates([0,0,1,1,1,1,2,3,3])
print(ans)
