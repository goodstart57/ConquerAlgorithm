class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(-1, -len(digits)-1, -1):
            if digits[i]+1 > 9:
                digits[i] = 0
                if i <= -len(digits):
                    digits = [1] + digits
            else:
                digits[i] += 1
                break
        
        return digits