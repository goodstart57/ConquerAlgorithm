class Solution:
    def romanToInt(self, s: str) -> int:
        map_index = {
            "I" : 0, #    1
            "V" : 1, #    5
            "X" : 2, #   10
            "L" : 3, #   50
            "C" : 4, #  100
            "D" : 5, #  500
            "M" : 6, # 1000
        }
        numbers = [1, 5, 10, 50, 100, 500, 1000]
        result = numbers[map_index.get(s[-1])]
        # print(result)
        
        substring = s[0]
        for i_curr in range(len(s)-1):
            char_curr = s[i_curr]
            char_next = s[i_curr+1]
            # print(f"[{i_curr}] char_curr : {char_curr}, char_next : {char_next}")
            if map_index.get(char_curr) < map_index.get(char_next):
                result += numbers[map_index.get(char_curr)] * -1
            else:
                result += numbers[map_index.get(char_curr)]
        
        return result