package leetcode;

/**
 * @author ytjia created on 2017-09-12 16:34
 */
public class MergeTwoSortedLists {

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
   * Merge two sorted linked lists and return it as a new list. The new list should be made by
   * splicing together the nodes of the first two lists.
   * <p>
   * https://leetcode.com/problems/merge-two-sorted-lists/description/
   */
  class Solution {

    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
      if (l1 == null && l2 == null) {
        return null;
      }
      ListNode preHead = new ListNode(0);
      ListNode curNode = preHead;
      while (l1 != null && l2 != null) {
        if (l1.val > l2.val) {
          curNode.next = l2;
          l2 = l2.next;
          curNode = curNode.next;
        } else {
          curNode.next = l1;
          l1 = l1.next;
          curNode = curNode.next;
        }

      }
      if (l1 == null) {
        curNode.next = l2;
      } else {
        curNode.next = l1;
      }

      return preHead.next;
    }
  }

}
