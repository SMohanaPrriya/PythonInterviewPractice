# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, first: Optional[ListNode], second: Optional[ListNode]) -> Optional[ListNode]:
        if first is None and second is None:
            return None
        if first is None or second is None:
            return first if first else second

        dummy = ListNode(0)
        head = dummy

        while first and second:
            if first.val <= second.val:
                dummy.next = first
                first = first.next
            else:
                dummy.next = second
                second = second.next
            dummy = dummy.next

        if first:
            dummy.next = first

        if second:
            dummy.next = second

        return head.next


        