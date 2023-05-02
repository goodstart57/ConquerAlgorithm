# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        for _ in range(k): # 남은 개수가 k개 이하면 뒤집지 않음
            if not curr:
                return head
            curr = curr.next
        
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            print(f"{prev.val} => ", end="")
        print()
        
        head.next = self.reverseKGroup(curr, k) #?
        
        return prev #?
    """
    def dfs(self, head):
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        i, node = 0, head
        sub, sub_last = ListNode(None, None), ListNode(None, None)
        prev = sub
        
        while node:
            node_next = node.next
            # sub - node - sub.next
            i, sub.next, node.next = i+1, node, sub.next
            
            if i == 1: 
                sub_last = node
            
            if i == k:
                i, sub = 0, sub_last
                
            node = node_next
        
        while prev:
            print(f"{prev.val} => ", end="")
            prev = prev.next
        return prev.next"""