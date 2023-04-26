class Solution:
    def countAndSay(self, n: int) -> str:
        dp = [ "" for i in range(0,n+1)]
        dp[1] = "1 "
        i = 2 ;
        while( i < n+1 ):
            print(f'i:{i} dp[{i-1}]:{dp[i-1]}')
            c = 0 
            for j in range(0,len(dp[i-1])-1):
                if( dp[i-1][j] == dp[i-1][j+1]):
                    c += 1;
                else:
                    dp[i] += chr(c+1+ord('0')) + dp[i-1][j] ;
                    c=0;
            dp[i] += ' ';
            i +=1
            

        return dp[-1][:-1];
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