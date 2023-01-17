class Solution:
    def reverse(self, x: int) -> int:
        result = int("-" + str(x)[1:][::-1] if x < 0 else str(x)[::-1])
        
        if not(pow(-2,31) < result < pow(2, 31) - 1):
            result = 0
        
        return result