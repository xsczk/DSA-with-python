"""Convert a non-negative integer num to its English words representation.

constrains: 0 <= num <= 2^31 - 1 (2,147,483,647)
"""


class Solution:
    # Time complexity: O(log(num)) because the number is divided by 1000 in each iteration
    # Space complexity: O(log(num))
    def number_to_words(self, num: int) -> str:
        if num == 0: return 'Zero'
        # 1234567
        # one million two hundred thirty four thousand five hundred sixty seven
        ones_map = {
            0: "",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
        }
        tens_map = {
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
        }

        def hundred_to_word(n: int) -> str:
            hundreds = n // 100
            # 123
            # res = ["One Hundred", "Twenty Three"]
            res = []
            # if n has a hundred unit
            if hundreds:
                res.append(ones_map[hundreds] + " Hundred")
            tens = n % 100
            # if tens >= 20, we take tens unit at tens_map or ones_map otherwise
            if tens >= 20:
                unit = tens % 10
                last_2 = tens_map[tens - unit]
                # append unit if it has
                if unit:
                    last_2 += " " + ones_map[unit]
            else:
                last_2 = ones_map[tens]
            if last_2:
                res.append(last_2)
            return " ".join(res)

        # first unit is an empty string to account for the case at the unit level
        units = ["", " Thousand", " Million", " Billion"]
        # 1023
        # reversed res = ["One Thousand", "Twenty Three"]
        res = []
        i = 0
        while num:
            # group the number by thousands (3 digits)
            digits = num % 1000
            # calc the remaining num
            num //= 1000
            s = hundred_to_word(digits)
            if s: res.append(s + units[i])
            i += 1
        res.reverse()
        return " ".join(res)


solution = Solution()
words = solution.number_to_words(12000023)
print(words)
