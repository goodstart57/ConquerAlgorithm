class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1
        if target in nums:
            result = nums.index(target)
        
        return result