class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = 0
        merged_arr = sorted(nums1 + nums2)
        
        if len(merged_arr) % 2 == 1: # 홀수면
            result = merged_arr[len(merged_arr)//2]
        else: # 짝수면
            result = (merged_arr[len(merged_arr)//2] + merged_arr[len(merged_arr)//2-1]) / 2
            
        return result