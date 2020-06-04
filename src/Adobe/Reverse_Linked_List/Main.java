package Adobe.Reverse_Linked_List;

public class Main {

    public static void main(String args[]) {

    }

    public class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

    public ListNode reverseList(ListNode head) {

        ListNode temp = head;

        ListNode reverseList = new ListNode();
        reverseList = reverseList.next;

        while (temp != null) {
            ListNode newNode = new ListNode(temp.val);
            newNode.next = reverseList;
            reverseList = newNode;
            temp = temp.next;
        }
        return reverseList;
    }

}
