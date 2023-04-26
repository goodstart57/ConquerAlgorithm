class Solution:
    def count(self, s):
        si, ei, result = 0, 0, []
        while ei + 1 < len(s):
            if s[ei] != s[ei + 1]:
                result.append(str(ei - si + 1))
                result.append(s[si])
                si = ei = ei + 1
            else:
                ei += 1
        result.append(str(ei - si + 1))
        result.append(s[si])
        return "".join(result)

    def countAndSay(self, n: int) -> str:
        i, result = 3, "11"
        if n == 1:
            return "1"
        elif n == 2:
            return "11"

        while i <= n:
            result = self.count(result)
            i += 1
        return result
