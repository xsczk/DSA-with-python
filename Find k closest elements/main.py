"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

Constraints:
- 1 <= k <= arr.length
- 1 <= arr.length <= 104
- arr is sorted in ascending order.
- -10^4 <= arr[i], x <= 10^4
"""


class Solution:
    def find_closest_elements(self, arr: list[int], k: int, x: int) -> list[
        int]:
        # define two pointers that are the first element's index of the window
        # which has k length can be formed. left is the first window, right is the last
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            # -----arr[mid]---x---------arr[mid + k]
            if x - arr[mid] <= arr[mid + k] - x:
                # move mid to the left
                right = mid
            else:
                left = mid + 1
        return arr[left: left + k]
