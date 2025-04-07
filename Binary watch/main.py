"""A binary watch has 4 LEDs on the top to represent the hours (0-11),
and 6 LEDs on the bottom to represent the minutes (0-59).
Each LED represents a zero or one, with the least significant bit on the right.

Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM),
return all possible times the watch could represent. You may return the answer in any order.

The hour must not contain a leading zero.

For example, "01:00" is not valid. It should be "1:00".
The minute must consist of two digits and may contain a leading zero.

For example, "10:2" is not valid. It should be "10:02".
"""


class Solution:
    def read_binary_watch(self, turned_on: int) -> list[str]:
        ans = []
        time = "0000000000"  # the first four 0s are hours and remaining six 0s are minutes

        def backtrack(led: int, index: int, bin_watch: str):
            if led == 0:
                # convert binary format value to hour and minute in 10 format value
                m = int(bin_watch[4:], 2)
                h = int(bin_watch[:4], 2)
                # ignore if h equal or greater than 12
                if h >= 12: return
                # format the time based on minute value
                if m < 10:
                    ans.append(str(h) + ":0" + str(m))
                elif m < 60:
                    ans.append(str(h) + ":" + str(m))
                return
            for i in range(index, 10):
                if bin_watch[i] == "0":
                    bin_watch = bin_watch[:i] + "1" + bin_watch[i + 1:]  # change
                    backtrack(led - 1, i + 1, bin_watch)  # recursive
                    bin_watch = bin_watch[:i] + "0" + bin_watch[i + 1:]  # backtrack

        if turned_on > 8:
            return ans  # no possible solution
        backtrack(turned_on, 0, time)
        return ans


solution = Solution()
ans = solution.read_binary_watch(2)
print(ans)
