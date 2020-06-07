# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        temp = head
        reverse_list = ListNode()
        reverse_list = reverse_list.next

        while temp is not None:
            new_node = ListNode(head.val)
            new_node.next = reverse_list
            reverse_list = new_node
            temp = temp.next

        return reverse_list
