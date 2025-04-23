"""You have a list arr of all integers in the range [1, n] sorted in a strictly increasing order.
Apply the following algorithm on arr:

- Starting from left to right, remove the first number and every other number afterward
until you reach the end of the list.
- Repeat the previous step again, but this time from right to left,
remove the rightmost number and every other number from the remaining numbers.
- Keep repeating the steps again, alternating left to right and right to left,
until a single number remains.

Given the integer n, return the last number that remains in arr."""


class Solution:
    # Time complexity: O(log n)
    # Space complexity: O(1)
    def last_remaining(self, n: int) -> int:
        remain = n
        step = 1
        left_to_right = True
        last = 1

        while remain > 1:
            # if the direction to eliminate is from left to right,
            # or the remaining items number is odd, update the value of last item
            if left_to_right or remain % 2 != 0:
                last += step
            # update step, remain and left_to_right for next elimination
            step *= 2
            remain //= 2
            left_to_right = not left_to_right
        return last

    # recursion based on iterative approach above
    # Time complexity: O(log n)
    # Space complexity: O(log n) due to recursion stack
    def last_remaining_2(self, n: int) -> int:

        def find_last(head: int, step: int, remaining_items: int, is_left_to_right: bool) -> int:
            if remaining_items < 2: return head
            head += step if remaining_items % 2 or is_left_to_right else 0
            step *= 2
            return find_last(head, step, remaining_items // 2, not is_left_to_right)

        return find_last(head=1, step=1, remaining_items=n, is_left_to_right=True)

solution = Solution()
last_item = solution.last_remaining_2(9)
print(last_item)