class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoSortedLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #to escape the edge case of inserting to an empty list
        tail = ListNode()
        output = tail
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
            tail = tail.next
        if l2:
            tail.next = l2

        return output.next


l1 = ListNode(1, None)
l1.next = ListNode(2, None)
l1.next.next = ListNode(3, None)

l2 = ListNode(1, None)
l2.next = ListNode(3, None)
l2.next.next = ListNode(4, None)
l2.next.next.next = ListNode(10, None)

s = Solution()
result = s.mergeTwoSortedLists(l1, l2)

while result:
    print(result.val, end='')
    if result.next:
        print("->", end='')
    result = result.next


