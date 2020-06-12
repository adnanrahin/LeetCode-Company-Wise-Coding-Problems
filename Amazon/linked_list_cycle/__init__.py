# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        fast_ptr = head
        slow_ptr = head

        while fast_ptr is not None and fast_ptr.next is not None:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
            if fast_ptr == slow_ptr:
                return True

        return False
