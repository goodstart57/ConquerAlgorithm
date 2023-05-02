class Solution:
    def arraySign(self, nums: List[int]) -> int:
        nums = sorted(nums)
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            # print(f"{l} / {m} / {r}")
            if nums[m] == 0:
                return 0
            elif nums[m] < 0:
                l = m + 1
            else:
                r = m
        return 1 if l % 2 == 0 else -1
        
        
    """def arraySign(self, nums: List[int]) -> int:
        result = 1
        for num in nums:
            if num == 0:
                return num
            result *= num
        return 1 if result > 0 else -1"""