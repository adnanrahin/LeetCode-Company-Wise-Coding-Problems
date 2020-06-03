package Adobe.Merge_Two_Sorted_Lists;

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

    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {

        ListNode solution = new ListNode();
        ListNode temp = solution;

        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                temp.next = new ListNode(l1.val);
                temp = temp.next;
                l1 = l1.next;
            } else if (l1.val > l2.val) {
                temp.next = new ListNode(l2.val);
                temp = temp.next;
                l2 = l2.next;
            } else if (l1.val == l2.val) {
                temp.next = new ListNode(l1.val);
                temp = temp.next;
                temp.next = new ListNode(l2.val);
                temp = temp.next;
                l1 = l1.next;
                l2 = l2.next;
            }
        }

        ListNode newNode = (l1 == null) ? l2 : l1;

        while (newNode != null) {
            temp.next = new ListNode(newNode.val);
            temp = temp.next;
            newNode = newNode.next;
        }


        return solution.next;

    }

}
