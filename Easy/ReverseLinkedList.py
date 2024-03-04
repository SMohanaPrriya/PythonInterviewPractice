class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def reverseLinkedList(self, head: ListNode) -> ListNode:
        prev, next, curr = None, None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def printList(self, l: ListNode):
        if not l:
            print("Empty list")
        while l:
            print(l.value,end='')
            if l.next:
                print("->",end='')
            l = l.next
        print()


l1 = ListNode(1, None)
l1.next = ListNode(90, None)
l1.next.next = ListNode(3, None)
l1.next.next.next = ListNode(10, None)

s = Solution()
s.printList(l1)
result = s.reverseLinkedList(l1)
s.printList(result)
