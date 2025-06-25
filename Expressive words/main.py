"""
Sometimes people repeat letters to represent extra feeling. For example:

- "hello" -> "heeellooo"
- "hi" -> "hiiii"
In these strings like "heeellooo", we have groups of adjacent letters
that are all the same: "h", "eee", "ll", "ooo".

You are given a string s and an array of query strings words.
A query word is stretchy if it can be made to be equal to s
by any number of applications of the following extension operation:
choose a group consisting of characters c, and add some number of characters c
to the group so that the size of the group is three or more.

For example, starting with "hello", we could do an extension on the group "o"
to get "hellooo", but we cannot get "helloo" since the group "oo" has a size less than three.
Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".
If s = "helllllooo", then the query word "hello" would be stretchy
because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.

Return the number of query strings that are stretchy.

Constraints:
- 1 <= s.length, words.length <= 100
- 1 <= words[i].length <= 100
- s and words[i] consist of lowercase letters.
"""
import itertools
from typing import Iterator


class Solution:
    # two pointers, Run Length Encoding
    # - time complexity: O(n * k) where n is the length of words list,
    # k is maximum length of the word
    # - space complexity: O(k) due to group and count list
    def expressive_words(self, s: str, words: list[str]) -> int:
        def RLE(S: str) -> tuple[list[str], list[int]]:
            """return the group of consecutive character of S in group
            and the number of each character appearance in count
            Ex: S = 'heeellooo' -> group: ['h', 'e', 'l', 'o'], count: [1, 3, 2, 3]
            """
            group, count, i, n = [], [], 0, len(S)
            while i < n:
                c = S[i]
                j = i
                while j < n and S[j] == c:
                    j += 1
                group.append(c)
                count.append(j - i)
                i = j
            return group, count

        R, count = RLE(s)
        ans = 0
        for word in words:
            R2, count2 = RLE(word)
            # if group2 not equal to group, that means word cannot be stretch to S
            # as they don't have the same characters
            if R2 != R:
                continue
            is_stretchy = True
            for i in range(len(count)):
                # if character's appearance of s smaller than its appearance in word
                # otherwise, if its appearance in s < 3 or they are equal
                # that means word cannot be stretched to s
                if (count[i] < count2[i]) or not (
                        count[i] >= 3 or count[i] == count2[i]):
                    is_stretchy = False
                    break
            if is_stretchy:
                ans += 1
        return ans

    # concise version based on the logic of above approach using groupby and zip
    def expressive_words_2(self, s: str, words: list[str]) -> int:
        def RLE(S: str) -> Iterator[tuple[str, int]]:
            return zip(*[(c, len(list(g))) for c, g in itertools.groupby(S)])

        R, count = RLE(s)
        ans = 0
        for word in words:
            R2, count2 = RLE(word)
            if R2 != R:
                continue
            ans += all(
                [c >= max(c2, 3) or c == c2 for c, c2 in zip(count, count2)])
        return ans


solution = Solution()
print(solution.expressive_words_2(s="heeellooo", words=["hello", "hi", "helo"]))
