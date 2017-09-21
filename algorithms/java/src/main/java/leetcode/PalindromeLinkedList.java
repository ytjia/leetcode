package leetcode;

/**
 * @author ytjia created on 2017-09-20 16:21
 */
public class PalindromeLinkedList {

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
   * Given a singly linked list, determine if it is a palindrome.
   * <p>
   * https://leetcode.com/problems/palindrome-linked-list/description/
   */
  class Solution {

    public boolean isPalindrome(ListNode head) {
      if (head == null) {
        return true;
      }
      ListNode curNode = head;
      int counter = 0;
      while (curNode != null) {
        curNode = curNode.next;
        counter++;
      }
      int mid = counter >> 1;
      counter = 0;
      ListNode pre = new ListNode(0);
      pre.next = head;
      ListNode tmp;
      curNode = head;
      while (curNode != null) {
        tmp = curNode.next;
        if (++counter > mid) {
          curNode.next = pre;
        }
        pre = curNode;
        curNode = tmp;
      }
      for (int i = 0; i < mid; i++) {
        if (head.val == pre.val) {
          head = head.next;
          pre = pre.next;
        } else {
          return false;
        }
      }
      return true;
    }
  }

}
