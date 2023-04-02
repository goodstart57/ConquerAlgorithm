class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (-1 if dividend < 0 else 1) * (-1 if divisor < 0 else 1)
        value = abs(dividend) // abs(divisor)
        
        if sign > 0 and value >= 2**31:
            value = 2**31 - 1
        elif sign < 0 and value > 2 ** 31:
            value = 2**31
        
        return sign * value