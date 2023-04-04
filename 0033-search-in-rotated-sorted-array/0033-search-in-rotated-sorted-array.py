class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result, l, r = -1, 0, len(nums) -1 
        while l <= r:
            mid = (r + l) // 2
            print(f"nums[{l}]:{nums[l]} / nums[{mid}]: {nums[mid]} / nums[{r}]: {nums[r]}")
            if nums[mid] == target:
                result = mid
            
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    # print("  # case1-1")
                    r = mid - 1
                else:
                    # print("  # case1-2")
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    print("  # case2-1")
                    l = mid + 1
                else:
                    print("  # case2-2")
                    r = mid - 1
        
        return result

## CLEAR
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         result = -1
#         if target in nums:
#             result = nums.index(target)
        
#         return result