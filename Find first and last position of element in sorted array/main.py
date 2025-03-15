"""Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity."""


# Time complexity: O(logn)
# Space complexity: O(1)
class Solution:
    def find_position(self, nums: list[int], target: int) -> list[int]:
        if not nums or nums[0] > target or nums[-1] < target:
            return [-1, -1]
        first = self.find_first(nums, target)
        last = self.find_last(nums, target)
        return [first, last]

    def find_first(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid - 1] != target:
                    return mid
                r = mid - 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1

    def find_last(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    return mid
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1


solution = Solution()
result = solution.find_position(nums=[2, 2], target=2)
print(result)
