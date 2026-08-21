class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while (b & mask) != 0:
            sum_without_carry = (a ^ b) & mask

            carry = ((a & b) << 1) & mask

            a = sum_without_carry
            b = carry
        
        max_int = 0x7FFFFFFF
        return a if a <= max_int else ~(a ^ mask)