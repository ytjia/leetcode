package leetcode;

/**
 * @author ytjia created on 2017-09-14 18:22
 */
public class RemoveNthNodeFromEndofList {

  /**
   * Definition for singly-linked list.
   */
  public class ListNode {

    int val;
    ListNode next;

    ListNode(int x) {
      val = x;
    }
  }

  /**
   * Given a linked list, remove the nth node from the end of list and return its head.
   * <p>
   * https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
   */
  class Solution {

    public ListNode removeNthFromEnd(ListNode head, int n) {
      ListNode preHead = new ListNode(0);
      preHead.next = head;
      ListNode firstNode = preHead;
      ListNode secondNode = preHead;
      for (int i = 0; i < n; i++) {
        firstNode = firstNode.next;
      }
      while (firstNode.next != null) {
        firstNode = firstNode.next;
        secondNode = secondNode.next;
      }
      secondNode.next = secondNode.next.next;

      return preHead.next;
    }
  }

}
