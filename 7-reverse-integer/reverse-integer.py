class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0

        while x > 0:
            digit = x % 10
            x //= 10

            rev = rev * 10 + digit

            if rev > 2147483647:
                return 0

        return sign * rev