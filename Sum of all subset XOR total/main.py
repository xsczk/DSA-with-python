"""The XOR total of an array is defined as the bitwise XOR of all its elements,
or 0 if the array is empty.

For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
Given an array nums, return the sum of all XOR totals for every subset of nums.

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b
by deleting some (possibly zero) elements of b.

"""



class Solution:
    def subset_XOR_sum(self, nums: list[int]) -> int:
        def xor_sum(nums: list[int], index: int, current_xor: int) -> int:
            # Return current_xor when all elements in nums are already considered
            if index == len(nums): return current_xor

            # Calculate sum of subset xor with current element
            with_element = xor_sum(nums, index + 1, current_xor ^ nums[index])

            # Calculate sum of subset xor without current element
            without_element = xor_sum(nums, index + 1, current_xor)

            # Return sum of xor totals
            return with_element + without_element

        return xor_sum(nums, index=0, current_xor=0)


solution = Solution()
ans = solution.subset_XOR_sum([5, 1, 6])
print(ans)
