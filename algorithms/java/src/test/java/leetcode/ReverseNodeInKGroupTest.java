package leetcode;

import org.junit.Test;

import leetcode.ReverseNodesInKGroup.ListNode;
import leetcode.ReverseNodesInKGroup.Solution;

/**
 * Created by ytjia on 15/12/28.
 */
public class ReverseNodeInKGroupTest {

  @Test
  public void reverseNodeInKGroup() {
    ReverseNodesInKGroup f = new ReverseNodesInKGroup();
    Solution s = f.new Solution();

    ListNode a = f.new ListNode(1);
    ListNode b = f.new ListNode(2);
    ListNode c = f.new ListNode(3);
    ListNode d = f.new ListNode(4);
    ListNode end = f.new ListNode(0);
    a.next = null;
    b.next = c;
    c.next = d;
    d.next = end;

//    s.reverseInGroup(null, a, d);
//
//    System.out.println(a.next.val);
//    System.out.println(b.next.val);
//    System.out.println(c.next.val);

    s.reverseKGroup(a, 1);
    System.out.println(b.next.val);
    System.out.println(c.next.val);
    System.out.println(d.next.val);
  }

}
