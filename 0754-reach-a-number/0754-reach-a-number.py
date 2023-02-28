class Solution:
    def reachNumber(self, target: int) -> int:
        S, k, delta = 0, 0, 1
        target = target if target > 0 else -target
        
        while True:
            if S < target:
                S, k = S+k+1, k+1
            else:
                delta = S - target
                
                if delta % 2 == 0:
                    break
                elif delta % 2 == 1:
                    S, k = S+k+1, k+1
                    
        return k
                