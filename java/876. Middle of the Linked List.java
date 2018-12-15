/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode fast = new ListNode( 0 );
        ListNode slow = new ListNode( 0 );
        
        fast = head;
        slow = head;
        
        while(fast.next != null && fast != null) { //停止条件
            fast = fast.next;
            fast = fast.next;
            slow = slow.next;
        }
        return slow.val; 
    }
}