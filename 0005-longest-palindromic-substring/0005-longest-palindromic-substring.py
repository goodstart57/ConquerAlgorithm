class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)

        if length == 1:
            return s
        
        for length_substring in range(length, 0, -1):
            for i_start in range(length - length_substring + 1):
                if s[i_start:i_start+length_substring] == s[i_start:i_start+length_substring][::-1]:
                    return s[i_start:i_start+length_substring]
        
        return ""