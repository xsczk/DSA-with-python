"""
Given string num representing a non-negative integer num, and an integer k,
return the smallest possible integer after removing k digits from num.

Example 1:
- Input: num = "1432219", k = 3
- Output: "1219"
- Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219
which is the smallest.

Example 2:
- Input: num = "10200", k = 1
- Output: "200"
- Explanation: Remove the leading 1 and the number is 200.
Note that the output must not contain leading zeroes.

Example 3:
- Input: num = "10", k = 2
- Output: "0"
- Explanation: Remove all the digits from the number and it is left with nothing which is 0.

Constraints:
- 1 <= k <= num.length <= 10^5
- num consists of only digits.
- num does not have any leading zeros except for the zero itself.
"""


class Solution:
    # use a greedy monotonic increasing stack: pop larger previous digits
    # when a smaller digit appears.
    # time complexity: O(n)
    # space complexity: O(n)
    def remove_k_digits(self, num: str, k: int) -> str:
        inc_st = []
        i = 0
        while i < len(num) and k > 0:
            # pop the larger previous digits and push the current digit afterward
            # to maintain the stack non-decreasing
            while inc_st and inc_st[-1] > num[i] and k > 0:
                inc_st.pop()
                k -= 1
            inc_st.append(num[i])
            i += 1
        # if we didn't scan the whole num, append the rest counting from num[i] to the stack
        if i < len(num):
            inc_st.append(num[i:])
        # if k is still > 0, we remove k digits from the end of the monotonic stack
        while inc_st and k > 0:
            inc_st.pop()
            k -= 1
        # remove leading zeros since the answer is not allowed
        res = ''.join(inc_st).lstrip('0')
        return res or '0'
