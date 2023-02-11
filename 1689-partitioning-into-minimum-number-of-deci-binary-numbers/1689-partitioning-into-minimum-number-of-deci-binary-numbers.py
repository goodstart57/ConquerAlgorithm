class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(list(n)))
    
    """
    def minPartitions(self, n: str) -> int:
        return sorted(map(lambda x: int(x), list(n)), key=lambda x: -x)[0]
    """