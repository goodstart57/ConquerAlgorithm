class Solution:
#     # 풀이 1
#     def longestPalindrome(self, s: str) -> str:
#         """solve with brute force"""
#         length = len(s)

#         if length == 1:
#             return s
        
#         for length_substring in range(length, 0, -1):
#             for i_start in range(length - length_substring + 1):
#                 if s[i_start:i_start+length_substring] == s[i_start:i_start+length_substring][::-1]:
#                     return s[i_start:i_start+length_substring]
        
#         return ""
    def longestPalindrome(self, s: str) -> str:
        """solve with dp"""
        substring = ""
        dp = [[0] * len(s) for _ in range(len(s))]
        
        for i in range(len(s)):
            dp[i][i] = True
            substring = s[i]
        
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    # print(f"({i}:{s[i]},{j}:{s[j]}) {s[i:j+1]}")
                    if j - i == 1 or dp[i+1][j-1] == True:
                        # print("  Accepted")
                        dp[i][j] = True
                        substring = max(substring, s[i:j+1], key=lambda x: len(x))
        return substring
        
        
        
        
        
        