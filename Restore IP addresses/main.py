"""A valid IP address consists of exactly four integers separated by single dots.
Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses,
but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses
that can be formed by inserting dots into s. You are not allowed to reorder or
remove any digits in s. You may return the valid IP addresses in any order."""


# backtracking
class Solution:
    def restore_ip_addresses(self, s: str) -> list[str]:
        n = len(s)
        res = []

        def backtrack(i: int, cur: str, count_dot: int):
            if count_dot == 3:
                if i < n and s[i] == '0' and len(s[i:]) > 1:
                    return
                if i < n and 0 <= int(s[i:]) <= 255:
                    res.append(cur + s[i:])
                return

            for j in range(i, min(i + 3, n)):
                temp = s[i:j + 1]
                if temp[0] == '0' and len(temp) > 1:
                    break
                if 0 <= int(s[i:j + 1]) <= 255:
                    backtrack(j + 1, cur + temp + '.', count_dot + 1)

        backtrack(0, '', 0)
        return res

    def restore_ip_addresses_2(self, s: str) -> list[str]:
        ans = []
        n = len(s)
        def backtrack(cur_ip: list[str], i: int):
            # the valid ip address contains exactly 4 integers
            if len(cur_ip) == 4:
                # only add to answer if all ip element
                # connect together will reach the end of the s
                if i == n:
                    ans.append('.'.join(cur_ip))
                return
            for j in range(i + 1, i + 4):
                temp = s[i:j]
                # j <= n: prevent temp to be empty
                # temp must be in range [1,255] (inclusive)
                # temp can be 0 alone but must not be any integer that have leading 0
                if (j <= n and 0 <= int(temp) <= 255 and not
                (temp[0] == '0' and len(temp) > 1)):
                    cur_ip.append(temp)
                    backtrack(cur_ip, j)
                    cur_ip.pop()

        backtrack(cur_ip=[], i=0)
        return ans


solution = Solution()
ans = solution.restore_ip_addresses_2(s='101023')
print(ans)
