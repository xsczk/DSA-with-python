"""You are playing a game involving a circular array of non-zero integers nums.
Each nums[i] denotes the number of indices forward/backward you must move
if you are located at index i:

- If nums[i] is positive, move nums[i] steps forward, and
- If nums[i] is negative, move nums[i] steps backward.
Since the array is circular, you may assume that moving forward from the last element
puts you on the first element, and moving backwards from the first element
puts you on the last element.

A cycle in the array consists of a sequence of indices seq of length k where:

- Following the movement rules above results in the repeating index sequence
seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
- Every nums[seq[j]] is either all positive or all negative.
- k > 1
Return true if there is a cycle in nums, or false otherwise."""


class Solution:
    # Floyd's Cycle detection
    # Time complexity:
    def circular_array_loop(self, nums: list[int]) -> bool:
        n = len(nums)

        # calculate the next index after moving from the previous index
        def next_index(i: int) -> int:
            return (i + nums[i]) % n

        for i in range(n):
            # define slow and fast pointers
            slow, fast = i, next_index(i)
            # skip self-loop
            if slow == fast:
                continue
            # keep looping to detect if there is a cycle in list nums.
            # If there is a num whose multiplication with previous num is a negative number,
            # then it cannot be a cycle
            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[next_index(fast)] > 0:
                if slow == fast:
                    # break if detect self-loop
                    if slow == next_index(slow):
                        break
                    return True
                slow = next_index(slow)
                fast = next_index(next_index(fast))

            # mark all elements in the current path as visited to avoid checking repeatedly
            j = i
            while nums[j] * nums[next_index(j)] > 0:
                temp = j
                j = next_index(j)
                # mark as visited
                nums[temp] = 0
        return False


solution = Solution()
is_cycle = solution.circular_array_loop([1, -1, 5, 1, 4])
print(is_cycle)
