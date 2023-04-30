class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates = sorted(candidates)
        
        def dfs(t, path):
            # print(f"target: {t} / path: {path}")
            if t < 0:
                # print("  cancel, t<0")
                return
            elif t == 0:
                # print("  Success, t=0")
                result.append(path)
                return
            
            for candidate in candidates:
                if not path or candidate >= path[-1]:
                    dfs(t-candidate, path + [candidate])
        
        dfs(target, [])
        return result
        