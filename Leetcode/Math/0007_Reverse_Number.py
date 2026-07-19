class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1

        s = str(abs(x))
        temp = ""

        for i in range(len(s) - 1, -1, -1):
            temp += s[i]

        ans = sign * int(temp)

        if ans < -2147483648 or ans > 2147483647:
            return 0

        return ans