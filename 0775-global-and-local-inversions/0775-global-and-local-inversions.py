class Solution:
    # def merge(nums):
#     def get_n_global_inversions(self, arr, n_gi):
#         # ★★★★★ 다 나누고 합칠때 비교함 이때 카운트를 할수있다 ★★★★★
#         if len(arr) < 2:
#             return arr, n_gi

#         mid = len(arr) // 2
#         low_arr, n_gi_low = self.get_n_global_inversions(arr[:mid], n_gi)
#         high_arr, n_gi_high = self.get_n_global_inversions(arr[mid:], n_gi)
#         n_gi = n_gi + n_gi_low + n_gi_high
        
#         merged_arr = []
#         l = h = 0
#         while l < len(low_arr) and h < len(high_arr):
#             if low_arr[l] < high_arr[h]:
#                 merged_arr.append(low_arr[l])
#                 l += 1
#             else:
#                 merged_arr.append(high_arr[h])
#                 h += 1
#                 n_gi += len(low_arr[l:])
#             # print(merged_arr, low_arr, high_arr)
#         merged_arr += low_arr[l:]
#         merged_arr += high_arr[h:]
#         return merged_arr, n_gi
    
#     def isIdealPermutation(self, nums: List[int]) -> bool:
#         n_gi, n_li = 0, 0
#         n = len(nums)
        
#         # local inversions
#         for i in range(len(nums)):
#             # case 1
#             if i+1 < n and nums[i] > nums[i+1]:
#                 n_li += 1
#         # global inversions
#         _, n_gi = self.get_n_global_inversions(nums, 0)
            
#             [2 0 1]
        
#         print(n_gi, n_li)
            
#         return n_gi == n_li    
    def isIdealPermutation(self, nums: List[int]) -> bool:
        num_max = -1
        for i in range(len(nums)-2):
            num_max = max(num_max, nums[i])
            if num_max > nums[i+2]:
                return False
        
        return True