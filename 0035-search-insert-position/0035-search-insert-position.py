class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # print(nums)
        length = len(nums) // 2
        i = length // 2
        # print(nums, "/ length : ", len(nums), " / target: ", target)
        # print(f"[{i}] nums[i]: {nums[i]} / length: {length}")
        while True:
            length = length // 2 if length > 1 else 1
            if nums[i] == target:
                break
            elif nums[i] > target: 
                if i == 0 or (i-1 > 0 and nums[i-1] < target):
                    break
                i -= length
            else: # nums[i] < target
                if i == len(nums)-1 or (i+1 > 0 and nums[i+1] > target):
                    i += 1
                    break
                i += length
        return i