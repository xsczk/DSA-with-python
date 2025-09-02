"""
Given a string s, remove duplicate letters so that every letter appears once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.

Note:
- A string a is lexicographically smaller than a string b if in the first position
where a and b differ, string a has a letter that appears earlier in the alphabet
than the corresponding letter in b.
If the first min(a.length, b.length) characters do not differ, then the shorter string
is the lexicographically smaller one.

Constraints:
- 1 <= s.length <= 10^4
- s consists of lowercase English letters.
"""


class Solution:
    # stack, hashtable, greedy
    def remove_duplicate_letters(self, s: str) -> str:
        visited = set()
        stack = []
        # find the last occurrence index of a letter in s
        last_occurrence = {letter: i for i, letter in enumerate(s)}
        for i, letter in enumerate(s):
            if letter in visited:
                continue
            """
            ff the top of the stack is greater than letter 
            and will occur later again, remove from stack
            """
            while stack and letter < stack[-1] and i < last_occurrence[
                stack[-1]]:
                visited.remove(stack.pop())
            stack.append(letter)
            visited.add(letter)
        return ''.join(stack)
