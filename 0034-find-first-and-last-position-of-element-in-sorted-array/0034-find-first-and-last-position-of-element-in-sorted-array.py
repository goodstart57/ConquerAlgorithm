class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums)        
        while l < r:
            m = (l + r) // 2
            # print(f"  [{l}/{m}/{r}] {nums[m]}")
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return l
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        
        if len(nums) == 0:
            return result
        
        result[0] = self.search(nums, target)
        result[1] = self.search(nums, target+1) - 1
        
        if result[0] > result[1]:
            result = [-1, -1]
        
        return result
    
    """def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        si, ei = 0, len(nums)-1
        # print(f"{nums}")
        while True:
            mi = (si + ei) // 2
            # print(f"  [{mi}] {nums[mi]}")
            if nums[mi] == target:
                # print(f"  case1 {si} {ei}")
                break
            elif si > ei:
                # print(f"  case2 {si} {ei}")
                mi = -1
                break 
            elif nums[mi] < target:
                si = mi + 1
                # print(f"  case3 {si} {ei}")
            else:
                ei = mi - 1
                # print(f"  case4 {si} {ei}")
        
        si = ei = mi
        
        if mi >= 0:
            while si > 0 and nums[si-1] == target: si -= 1
            while ei < len(nums)-1 and nums[ei+1] == target: ei += 1
            
        return [si, ei]"""