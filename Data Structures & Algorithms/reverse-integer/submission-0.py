class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT = -2**31
        MAX_INT = 2**31

        sign = -1 if x < 0 else 1
        x = abs(x)

        result = 0

        while x != 0:
            digit = x % 10

            result = (result * 10) + digit

            x = x // 10
        
        result *= sign

        if result < MIN_INT or result > MAX_INT:
            return 0
        return result
