class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        solution = ListNode(0)
        head = solution

        while l1 is not None and l2 is not None:

            if l1.val < l2.val:
                head.next = ListNode(l1.val)
                l1 = l1.next
                head = head.next
            elif l1.val > l2.val:
                head.next = ListNode(l2.val)
                l2 = l2.next
                head = head.next
            elif l1.val == l2.val:
                head.next = ListNode(l1.val)
                head = head.next
                head.next = ListNode(l2.val)
                head = head.next
                l1 = l1.next
                l2 = l2.next

        temp = l1 if l2 is None else l2

        while temp is not None:
            head.next = ListNode(temp.val)
            head = head.next
            temp = temp.next

        return solution.next
