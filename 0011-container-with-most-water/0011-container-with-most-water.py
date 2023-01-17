class Solution:
    """TRY#1 bruteforce
    def maxArea(self, height: List[int]) -> int:
        result = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                result = max(result, min(height[i], height[j]) * (j - i))
        return result
    """
    
    """TRY#2 greedy"""
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_size = -1
        
        while i != j:
            max_size = max(max_size, min(height[i], height[j]) * (j - i))
            
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return max_size