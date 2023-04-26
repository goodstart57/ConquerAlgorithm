class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1: return '1'
        
        res = ['1']
        for i in range(n-1):
            i = 0
            s = res[-1]
            curr_s = ''
            j = 0
            while i<len(s):
                c = 0
                while j<len(s) and s[i] == s[j]:
                    c+=1
                    j+=1
                curr_s += str(c)
                curr_s += str(s[i])
                i = j
                
            res.append(curr_s)
        
        return res[-1]
"""class Solution:
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
        return result"""