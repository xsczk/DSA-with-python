"""Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets
is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces,
square brackets are well-formed, etc. Furthermore, you may assume that
the original data does not contain any digits and that digits are only for those repeat numbers, k.
For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 10^5."""


class Solution:
    # recursive
    def decode_string(self, s: str) -> str:

        def decode(i: int) -> tuple[str, int]:
            result = ''
            while i < len(s) and s[i] != ']':
                if s[i].isalpha():
                    result += s[i]
                    # base case: s[i] is gonna to point to ']' at the end of the while loop
                    i += 1
                    continue
                num = ''
                while s[i].isdigit():
                    # build the repeat count
                    num += s[i]
                    i += 1
                # start looping at substring, s[i] will now point to the first char at the substr
                i += 1
                # retrieve i at recursive call,
                # i will now point to ']' at previous recursive callstack
                sub_str, i = decode(i)
                i += 1
                result += sub_str * int(num)
            return result, i

        return decode(0)[0]

    # stack
    def decode_string_2(self, s: str) -> str:
        stack = []
        cur = ''
        num = 0
        for char in s:
            # build the repeat count
            if char.isdigit():
                # num could be multi digit => multiply by 10 at each for loop
                num = num * 10 + int(char)
            elif char == '[':
                stack.append((cur, num))
                # reset cur and num for next bracket level
                cur = ''
                num = 0
            elif char == ']':
                prev, repeat = stack.pop()
                cur = prev + cur * repeat
            else:
                cur += char
        return cur

solution = Solution()
decoded = solution.decode_string_2("3[a2[c]]")
print(decoded)