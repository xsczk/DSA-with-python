"""Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons)
is given below. Note that 1 does not map to any letters."""


class Solution:
    def letter_combinations(self, digits: str) -> list[str]:
        ans = []
        if len(digits) == 0: return ans
        digit_to_str = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        self.backtracking(ans=ans, digit_to_str=digit_to_str, i=0, combination='', digits=digits)
        return ans

    def backtracking(self, ans: list[str], digit_to_str: dict[str, str], i: int, combination: str, digits: str) -> None:
        """

        :param ans: list of all possible combinations
        :param digit_to_str: dictionary specify the digits corresponding to number
        :param i: index keeps track of current digit
        :param combination: currently combination
        :param digits: input digits
        :return: None
        """
        # base case: our current combination has len equal to digits len
        if len(combination) == len(digits):
            ans.append(combination)
            return
        cur_digit = digits[i]
        cur_str = digit_to_str[cur_digit]
        for char in cur_str:
            combination += char
            self.backtracking(ans=ans, digit_to_str=digit_to_str, i=i + 1, combination=combination, digits=digits)
            combination = combination[:-1]
        return

solution = Solution()
ans = solution.letter_combinations(digits='23')
print(ans)
