package leetcode;

/**
 * Accepted.
 *
 * https://leetcode.com/problems/reverse-nodes-in-k-group/
 * Created by ytjia on 15/12/9.
 */
public class ReverseNodesInKGroup {

  public class ListNode {

    int val;
    ListNode next;

    ListNode(int x) {
      val = x;
    }
  }

  public class Solution {

    public ListNode reverseKGroup(ListNode head, int k) {
      ListNode cur = head;
      int length = 0;
      while (cur != null) {
        cur = cur.next;
        ++length;
      }
      if (length < k) {
        return head;
      }
      int stopIndex = length - (length % k);

      int i = 1;
      ListNode pre = null;
      ListNode post;
      ListNode groupHead = head;
      ListNode newHead = head;
      cur = head;
      while (i <= stopIndex) {
        if (i % k == 0) {
          if (i == k) {
            newHead = cur;
          }
          post = cur.next;
          reverseInGroup(pre, groupHead, post);
          pre = groupHead;
          cur = pre;
          groupHead = post;
        }
        cur = cur.next;
        ++i;
      }

      return newHead;
    }

    public void reverseInGroup(ListNode pre, ListNode cur, ListNode post) {
      ListNode preCur = post;
      while (cur != post) {
        ListNode tmp = cur.next;
        cur.next = preCur;
        preCur = cur;
        if (tmp == post) {
          if (pre != null) {
            pre.next = cur;
          }
          break;
        }
        cur = tmp;
      }
    }
  }
}
