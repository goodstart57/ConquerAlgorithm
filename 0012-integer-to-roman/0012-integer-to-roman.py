class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        for i in range(13):
            cnt, num = num // values[i], num % values[i]
            print(cnt, symbols[i], values[i], num)
            result += symbols[i]*cnt
        
        return result