class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums[:] = nums[:i] + nums[i+1:]
            else:
                i += 1
        