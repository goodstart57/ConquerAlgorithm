class Solution:
    def arraySign(self, nums: List[int]) -> int:
        result = 1
        for num in nums:
            if num == 0:
                return num
            result *= num
        return 1 if result > 0 else -1