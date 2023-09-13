# Definition for singly-linked list.
# class ListNode:
#     def _init_(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = head
        count = 0
        while cur:
            count +=1
            cur = cur.next
        res = head    
        for i in range(count//2):
            res = res.next
        return res