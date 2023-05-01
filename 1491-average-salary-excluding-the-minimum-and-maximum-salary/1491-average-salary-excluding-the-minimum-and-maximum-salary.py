class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)
    """def average(self, salary: List[int]) -> float:
        salary.sort()
        return sum(salary[1:-1]) / len(salary[1:-1])"""
    
    """def average(self, salary: List[int]) -> float:
        cnt, salary_sum, salary_max, salary_min = 0, 0, 0, 10**6+1
        for s in salary:
            cnt += 1
            salary_sum += s
            salary_max = max(s, salary_max)
            salary_min = min(s, salary_min)
        
        return (salary_sum - salary_max - salary_min) / (cnt - 2)"""