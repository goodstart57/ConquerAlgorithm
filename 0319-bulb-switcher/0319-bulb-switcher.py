class Solution:
    def bulbSwitch(self, n: int) -> int:
        result = 0
        # print(f"[{n}]")
        for i in range(1, n+1):
            # print("  ", i)
            if i*i <= n:
                result += 1
            else:
                break
        return result