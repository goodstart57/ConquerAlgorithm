# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(None, head)
        curr = head
        
        while True:
            if curr.next and curr.next.next:
                # print(f"before {curr}")
                curr.next, curr.next.next, curr.next.next.next = curr.next.next, curr.next, curr.next.next.next
                # print(f"after {curr}")
            
            if curr.next and curr.next.next and curr.next.next.next and curr.next.next.next.next:
                # print("go to next~")
                curr = curr.next.next
            else:
                break
                
        return head.next