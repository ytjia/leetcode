package leetcode;

/**
 * @author ytjia created on 2017-09-17 13:46
 */
public class LinkedListCycle2 {

  /**
   * Definition for singly-linked list.
   */
  class ListNode {

    int val;
    ListNode next;

    ListNode(int x) {
      val = x;
      next = null;
    }
  }

  /**
   * Given a linked list, return the node where the cycle begins. If there is no cycle, return
   * null.
   * <p>
   * https://leetcode.com/problems/linked-list-cycle-ii/description/
   */
  public class Solution {

    public ListNode detectCycle(ListNode head) {
      if (head == null || head.next == null) {
        return null;
      }

      ListNode stepOne = head.next;
      ListNode stepTwo = head.next.next;
      while (stepOne != stepTwo) {
        if (stepTwo == null || stepTwo.next == null) {
          return null;
        }
        stepOne = stepOne.next;
        stepTwo = stepTwo.next.next;
      }
      stepOne = head;
      while (stepOne != stepTwo) {
        stepOne = stepOne.next;
        stepTwo = stepTwo.next;
      }
      return stepOne;
    }
  }

}
