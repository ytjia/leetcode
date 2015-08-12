package leetcode;

/**
 * Accepted
 * https://leetcode.com/problems/intersection-of-two-linked-lists/
 * Created by ytjia on 15/8/4.
 */
public class IntersectionOfTwoLinkedLists {

  public class ListNode {

    int val;
    ListNode next;

    ListNode(int x) {
      val = x;
      next = null;
    }
  }

  public class Solution {

    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {

      int lengthA = 0;
      int lengthB = 0;

      ListNode nodeA = headA;
      ListNode nodeB = headB;

      while (nodeA != null) {
        nodeA = nodeA.next;
        lengthA++;
      }
      while (nodeB != null) {
        nodeB = nodeB.next;
        lengthB++;
      }

      ListNode nodeX, nodeY;
      if (lengthA >= lengthB) {
        nodeX = headA;
        nodeY = headB;
      } else {
        nodeX = headB;
        nodeY = headA;
      }

      int differ = java.lang.Math.abs(lengthA - lengthB);
      for (int i = 0; i < differ; i++) {
        nodeX = nodeX.next;
      }
      while (nodeX != null) {
        if (nodeX == nodeY) {
          return nodeX;
        }
        nodeX = nodeX.next;
        nodeY = nodeY.next;
      }

      return null;
    }
  }
}
