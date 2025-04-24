"""Alice and Bob are playing a game. Initially, Alice has a string word = "a".

You are given a positive integer k.

Now Bob will ask Alice to perform the following operation forever:

Generate a new string by changing each character in word
to its next character in the English alphabet, and append it to the original word.
For example, performing the operation on "c" generates "cd"
and performing the operation on "zb" generates "zbac".

Return the value of the k-th character in word, after enough operations have been done for word
to have at least k characters.

Note that the character 'z' can be changed to 'a' in the operation.

"""

class Solution:
    # iterative
    # Time complexity: O(k)
    # Space complexity: O(k) due to init_str
    def kth_character(self, k: int) -> str:
        init_str = 'a'
        while len(init_str) < k:
            cur = ''
            for char in init_str:
                # get the Unicode code from char
                unicode = ord(char)
                # convert the Unicode code to corresponding char
                generate_char = chr(unicode + 1)
                cur += generate_char if char != 'z' else 'a'
            init_str += cur
        return init_str[k - 1]

solution = Solution()
ans = solution.kth_character(9)
print(ans)