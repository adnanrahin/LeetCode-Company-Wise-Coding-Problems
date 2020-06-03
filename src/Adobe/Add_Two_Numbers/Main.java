package Adobe.Add_Two_Numbers;

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

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        if (l1 == null && l2 == null) {
            return null;
        }

        if (l1 != null && l2 == null)
            return l1;

        if (l2 != null && l1 == null)
            return l2;

        ListNode solution = new ListNode();

        ListNode head = solution;

        int carry = 0;

        while (l1 != null && l2 != null) {
            int sum = l1.val + l2.val + carry;
            int mod = sum % 10;
            carry = sum / 10;
            ListNode temp = new ListNode(mod);
            head.next = temp;
            head = head.next;
            l1 = l1.next;
            l2 = l2.next;
        }

        ListNode newNode = (l1 == null) ? l2 : l1;

        while (newNode != null) {
            int sum = newNode.val + carry;
            int mod = sum % 10;
            carry = sum / 10;
            ListNode temp = new ListNode(mod);
            head.next = temp;
            head = head.next;
            newNode = newNode.next;
        }

        if (carry != 0) {
            ListNode temp = new ListNode(carry);
            head.next = temp;
            head = head.next;
        }

        return solution;
    }

}
