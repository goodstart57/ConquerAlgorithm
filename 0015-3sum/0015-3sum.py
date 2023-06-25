class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        
        n, p, z = [], [], []
        
        for num in nums:
            if num > 0:
                p.append(num)
            elif num == 0:
                z.append(num)
            else: # num < 0
                n.append(num)
        
        N, P = set(n), set(p)
        
        # -n, 0, n
        if z:
            for num in P:
                if -num in N:
                    answer.add((-num, 0, num))
        
        # triple 0
        if len(z) > 2:
            answer.add((0, 0, 0))
                    
        # -num1, -num2, (num1+num2)
        for i1 in range(len(n)):
            for i2 in range(i1+1, len(n)):
                target = -(n[i1]+n[i2])
                if target in P:
                    answer.add(tuple(sorted((n[i1], n[i2], target))))
        
        # num1, num2, -(num1+num2)
        for i1 in range(len(p)):
            for i2 in range(i1+1, len(p)):
                target = -(p[i1]+p[i2])
                if target in N:
                    answer.add(tuple(sorted((target, p[i1], p[i2]))))

        return answer
        
        