from collections import deque,Counter
from pprint import pprint as pp

class Solution:
    def reorganizeString(self, s: str) -> str:
        self.s = list(s)
        self.s = Counter(self.s).items()
        self.s = sorted(self.s, key=lambda x: -x[1])
        self.s = [[k, v] for k, v in self.s]
        print(s, self.s)
        result, c_max_cnt = self.s[0]
        if c_max_cnt > len(s)//2 + len(s)%2:
            return ""

        i = 0
        self.s[i][1] -= 1
        if self.s[i][1] == 0:
            self.s.pop(i)
        self.s = sorted(self.s, key=lambda x: -x[1])

        while self.s:
            if result[-1] != self.s[0][0]:
                i = 0
            else:
                i = 1

            result += self.s[i][0]
            self.s[i][1] -= 1
            if self.s[i][1] == 0:
                self.s.pop(i)
            self.s = sorted(self.s, key=lambda x: -x[1])
                    
            print(f"  [{i}]", result, self.s)

        return result

"""
        
    def reorganizeString(self, s: str) -> str:
        s, s2 = deque(s), deque()
        result = s.popleft()
        
        while s:
            if s2 and result[-1] != s2[0]:
                result += s2.popleft()
            elif result[-1] == s[0]:
                s2.append(s.popleft())
            else:
                result += s.popleft()
            print(f"s:{s}, s2:{s2}, result:{result}")


        if s2 and result[-1] != s2[0]:
            result += s2.popleft()

        return result
"""

"""permutations
    def dfs(self, s):
        for substr in permutations(s):
            stack = deque(substr[0])
            for c in substr[1:]:
                if stack[-1] == c:
                    break
                else:
                    stack.append(c)
            
            if len(stack) == len(s):
                break
            else:
                stack = deque(s[0])
                
        return "".join(stack) if len(stack) == len(s) else ""
"""