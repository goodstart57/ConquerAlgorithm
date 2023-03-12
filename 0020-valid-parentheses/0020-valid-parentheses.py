class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        oppose = {")":"(", "}":"{", "]":"["}
        
        for c in s:
            if c in ("(", "{", "["):
                stack.append(c)
            elif not stack:
                return False
            elif not oppose.get(c) == stack.pop():
                return False
        
        return len(stack) == 0