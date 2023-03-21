class Solution:
    def dfs(self, p, o, c): # p : parenthesis / o : cnt of open p / c : cnt of closed p
        # print(f"[{self.i}] {p}")
        self.i += 1
        if o == c == self.n:
            # print(f"  appended")
            return [p]
        elif o > self.n or o < c:
            # print(f"  exit")
            return []
        return self.dfs(p + "(", o+1, c) + self.dfs(p + ")", o, c+1)
    
    def generateParenthesis(self, n: int) -> List[str]:
        self.i = 0
        self.n = n
        return self.dfs("(", 1, 0)
