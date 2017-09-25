package leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * @author ytjia created on 2017-09-25 16:17
 */
public class LRUCache {

  class DLinkedNode {

    int key;
    int value;
    DLinkedNode pre;
    DLinkedNode next;
  }

  private Map<Integer, DLinkedNode> cache = new HashMap<>();
  private int capacity;
  private DLinkedNode lruHead, lruTail;

  public LRUCache(int capacity) {
    this.capacity = capacity;

    lruHead = new DLinkedNode();
    lruTail = new DLinkedNode();

    lruHead.pre = null;
    lruHead.next = lruTail;

    lruTail.pre = lruHead;
    lruTail.next = null;
  }

  private void addNode(DLinkedNode node) {
    node.pre = lruHead;
    node.next = lruHead.next;

    lruHead.next.pre = node;
    lruHead.next = node;
  }

  private void removeNode(DLinkedNode node) {
    node.pre.next = node.next;
    node.next.pre = node.pre;
  }

  private void moveNodeToHead(DLinkedNode node) {
    removeNode(node);
    addNode(node);
  }

  public int get(int key) {
    if (cache.containsKey(key)) {
      DLinkedNode targetNode = cache.get(key);
      moveNodeToHead(targetNode);
      return targetNode.value;
    } else {
      return -1;
    }
  }

  public void put(int key, int value) {
    if (cache.containsKey(key)) {
      DLinkedNode node = cache.get(key);
      node.value = value;
      moveNodeToHead(node);
    } else {
      DLinkedNode newNode = new DLinkedNode();
      newNode.key = key;
      newNode.value = value;
      addNode(newNode);
      cache.put(key, newNode);

      if (cache.size() > capacity) {
        DLinkedNode lruNoe = lruTail.pre;
        cache.remove(lruNoe.key);
        removeNode(lruNoe);
      }
    }
  }

}
