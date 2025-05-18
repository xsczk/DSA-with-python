"""Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases,
more than once."""


class Solution:
    def reverse_vowels(self, s: str) -> str:
        vowels = ('a', 'e', 'i', 'o', 'u')
        l, r = 0, len(s) - 1
        s = list(s)
        while l < r:
            # move l forward until s[l] is a vowel
            while s[l].lower() not in vowels and l < r:
                l += 1
            # move r backward until s[r] is a vowel
            while s[r].lower() not in vowels and l < r:
                r -= 1
            # if l is already equal to r: break the loop (means there is no any vowels to swap)
            if l == r: break
            # swap two elements
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)


solution = Solution()
reversed_s = solution.reverse_vowels('leetcode')
print(reversed_s)

