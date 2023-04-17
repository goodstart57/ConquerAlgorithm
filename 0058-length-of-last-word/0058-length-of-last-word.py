class Solution:
    """
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
    """
    def lengthOfLastWord(self, s: str) -> int:
        result = 0
        s = s.strip()
        length = len(s)
        i = -1
        while i >= -length and s[i] != " ":
            result += 1
            i -= 1
        return result