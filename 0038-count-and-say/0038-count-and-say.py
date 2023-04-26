class Solution:
    def count(self, s):
        si, ei, result = 0, 0, ""
        while ei+1 < len(s):
            # print(f"({si}, {ei}) {s[si:ei+1]}")
            if s[ei] != s[ei+1]:
                result += f"{len(s[si:ei+1])}{s[si]}"
                si = ei = ei + 1
            else:
                ei += 1
        result += f"{len(s[si:ei+1])}{s[si]}"
        return result
    
    def countAndSay(self, n: int) -> str:
        i, result = 3, "11"
        if n == 1:
            return "1"
        elif n == 2:
            return "11"
        
        while i <= n:
            result = self.count(result)
            # print(f"[{i}] {result}")
            i += 1
        return result
        
        
        
        