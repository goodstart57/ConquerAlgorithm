class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        si, ti = 0, 0
        print(f"s: {s} / t: {t}")
        while si < len(s) or ti < len(t):
            if si == 0 and s[si] == "#":
                s = s[1:]
                si -= 1
            elif 0 < si < len(s) and s[si] == "#":
                s = s[:si-1] + s[si+1:]
                si = si -2
            
            
            if ti == 0 and t[ti] == "#":
                t = t[1:]
                ti -= 1
            elif 0 < ti < len(t) and t[ti] == "#":
                t = t[:ti-1] + t[ti+1:]
                ti = ti -2
            
            # print(f"s[{si}]: {s} / t[{ti}]: {t}")
            
            si += 1
            ti += 1
        return s == t