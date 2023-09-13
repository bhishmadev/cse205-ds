# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def _init_(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count=0
        if curr.next==None:
            return None 
        while curr:
            curr=curr.next
            count+=1
        curr = head
        if count-n ==0:
            return head.next
            while curr is not None:
                return curr
        for i in range(count-n-1):
            curr = curr.next
        curr.next=curr.next.next
        curr=head
        return curr