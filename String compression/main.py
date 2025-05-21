"""Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

- If the group's length is 1, append the character to s.
- Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead,
be stored in the input character array chars. Note that group lengths that are 10 or longer
will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space."""


class Solution:
    # two pointers
    # Time complexity: O(n) - each character is visited once
    # Space complexity: O(1) as we only use i and j as constant to traverse
    def compress(self, chars: list[str]) -> int:
        # define two pointers: i to traverse the list chars,
        # j is used to track and mutate chars in-place
        i, j = 0, 0
        res = 0
        while i < len(chars):
            cnt = 1
            # check current characters with the next character in chars
            # if they are equal, increase current cnt and i.
            # keep looping until this condition is satisfied
            while i + 1 < len(chars) and chars[i] == chars[i + 1]:
                cnt += 1
                i += 1
            # mutate chars directly with the character first
            chars[j] = chars[i]
            j += 1
            # auto +1 because we need to count the character
            res += 1
            if cnt > 1:
                str_cnt = str(cnt)
                str_len = len(str_cnt)
                # using slicing to mutate chars in-place, replace them with list of digits of cnt
                chars[j:j + str_len] = list(str_cnt)
                j += str_len
                res += str_len
            # increase i to keep looping
            i += 1
        return res


solution = Solution()
ans = solution.compress(["a", "a", "b", "b", "c", "c", "c"])
