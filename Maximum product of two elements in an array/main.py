"""Given the array of integers nums, you will choose two different indices i and j of that array.
Return the maximum value of (nums[i]-1)*(nums[j]-1)."""

class Solution:
    # sorting before calculating the result
    # Time complexity: O(nlog n) sorting causes n * log n time complexity
    # Space complexity: O(n)
    def max_product(self, nums: list[int]) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)

    # investigate the biggest and the second biggest of the array
    # Time complexity: O(n)
    # Space complexity: O(1)
    def max_product_2(self, nums: list[int]) -> int:
        biggest, second_biggest = 0, 0
        for num in nums:
            if num > biggest:
                # we have found a new biggest element and should update biggest = num.
                # however, before we do this, we update second_biggest = biggest
                # since the old biggest element we saw will become the new second biggest element.
                second_biggest = biggest
                biggest = num
            else:
                # should not update biggest. However, num may be larger than second_biggest,
                # in which case it would be the new second biggest element.
                # we update second_biggest with num if it is larger.
                second_biggest = max(second_biggest, num)
        return (biggest - 1) * (second_biggest - 1)

solution = Solution()
max_product_of_two = solution.max_product_2([3,4,5,2])
print(max_product_of_two)