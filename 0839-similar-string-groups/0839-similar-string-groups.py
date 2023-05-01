class Solution:
    def is_similar(self, s1, s2):
        cnt_diff = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                cnt_diff += 1
            if cnt_diff > 2:
                return False
        return True
    
    def dfs(self, i, strs, visited):
        visited[i] = True
        for j in range(len(strs)):
            if not visited[j] and self.is_similar(strs[i], strs[j]):
                self.dfs(j, strs, visited)
    
    def numSimilarGroups(self, strs: List[str]) -> int:
        degree = 0
        visited = [False] * len(strs)
        for i in range(len(strs)):
            if not visited[i]:
                self.dfs(i, strs, visited)
                degree += 1
        return degree
    
    
    """
    def is_sim(self, s1, s2):
        cnt_diff = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                cnt_diff += 1
            elif cnt_diff > 2:
                return False
        return True
    
    def numSimilarGroups(self, strs: List[str]) -> int:
        if len(strs) == 0:
            return 0
        elif len(strs) == 1:
            return 1
        
        i, degree, strs_groups = 0, 0, [0 for _ in range(len(strs))]
        for i in range(len(strs)):
            if strs_groups[i] > 0:
                tmp_degree = strs_groups[i]
            else:
                tmp_degree = degree+1
                strs_groups[i] = tmp_degree
            print(f"[degree: {degree}] i: {i} / strs[{i}]: {strs[i]} / strs_groups: {strs_groups}")
            
            for j in range(i+1, len(strs)):
                print(f"  j: {j} / strs[{j}]: {strs[j]}")
                if strs_groups[j] > 0:
                    print("    pass")
                    continue
                elif self.is_sim(strs[i], strs[j]):
                    if strs[j] > 0:
                        strs_groups[j] = tmp_degree
                    print("    sim")
                else:
                    print("    not sim")
        return degree"""
            
            