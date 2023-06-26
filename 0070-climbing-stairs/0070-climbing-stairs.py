"""
n = 2 / 2
1 1
2

n = 3 / 3
1 1 1
1 2
2 1

n = 4 /
1 1 1 1
1 1 2
1 2 1
2 1 1
2 2

1 1 1 1 1
1 1 1 1
1 1 2
1 2 1
2 1 1
2 2

"""


class Solution:
    def climbStairs(self, n: int) -> int:
        last1, last2 = [0 for _ in range(n+1)], [0 for _ in range(n+1)]
        last1[1] = 1
        
        for i in range(2, n+1):
            last1[i] += last1[i-1] + last2[i-1]
            last2[i] += last1[i-1]
            # print(f"[{n}] i: {i}")
        
        return last1[n] + last2[n]
        