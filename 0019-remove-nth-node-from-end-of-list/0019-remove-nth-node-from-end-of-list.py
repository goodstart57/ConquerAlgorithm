# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:            
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = [None for _ in range(30)]
        nodes[0] = head
        
        for i in range(1, 30+1):
            if nodes[i-1].next:
                nodes[i] = nodes[i-1].next
            else:
                nodes = nodes[:i]
                break
        
        nodes.pop(len(nodes)-(n))
        nodes.append(None)
        
        for i in range(1, len(nodes)):
            nodes[i-1].next = nodes[i]
        
        return nodes[0]