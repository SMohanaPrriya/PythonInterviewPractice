# Leet code : 234 Palindrome linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def printList(self, l: ListNode):
        if not l:
            print("Empty list")
        while l:
            print(l.val,end='')
            if l.next:
                print("->",end='')
            l = l.next
        print()

    def isPalindrome(self, head: ListNode) -> bool:
        fast, slow = head, head

        #find middle(slow pointer) and end(fast pointer)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse the list from mid/second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        self.printList(prev)

        #check for palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            else:
                left = left.next
                right = right.next
        return True


head = ListNode(1, None)
head.next = ListNode(2, None)
head.next.next = ListNode(2, None)
head.next.next.next = ListNode(2, None)
head.next.next.next.next = ListNode(1, None)

s = Solution()
s.printList(head)
print(s.isPalindrome(head))
