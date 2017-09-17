package leetcode;

/**
 * @author ytjia created on 2017-09-15 21:45
 */
public class ImplementTrie_PrefixTree {

  /**
   * Implement a trie with insert, search, and startsWith methods.
   * <p>
   * https://leetcode.com/problems/implement-trie-prefix-tree/description/
   */
  class Trie {

    private TrieNode root;

    /**
     * Initialize your data structure here.
     */
    public Trie() {
      root = new TrieNode();
    }

    /**
     * Inserts a word into the trie.
     */
    public void insert(String word) {
      String wordLowerCase = word.toLowerCase();
      TrieNode curNode = this.root;
      for (int i = 0; i < wordLowerCase.length(); i++) {
        char ch = wordLowerCase.charAt(i);
        if (!curNode.contains(ch)) {
          curNode.put(ch, new TrieNode());
        }
        curNode = curNode.get(ch);
      }
      curNode.setEnd();
    }

    private TrieNode getPrefix(String prefix) {
      TrieNode curNode = this.root;
      for (int i = 0; i < prefix.length(); i++) {
        char ch = prefix.charAt(i);
        if (!curNode.contains(ch)) {
          return null;
        }
        curNode = curNode.get(ch);
      }
      return curNode;
    }

    /**
     * Returns if the word is in the trie.
     */
    public boolean search(String word) {
      TrieNode node = getPrefix(word);
      return node != null && node.isEnd();
    }

    /**
     * Returns if there is any word in the trie that starts with the given prefix.
     */
    public boolean startsWith(String prefix) {
      return getPrefix(prefix) != null;
    }
  }

  class TrieNode {

    private static final int ALPHABET_SIZE = 26;
    private TrieNode[] children;
    private boolean endStatus;

    public TrieNode() {
      children = new TrieNode[ALPHABET_SIZE];
    }

    public void setEnd() {
      endStatus = true;
    }

    public boolean isEnd() {
      return endStatus;
    }

    public void put(char ch, TrieNode node) {
      children[ch - 'a'] = node;
    }

    public boolean contains(char ch) {
      return children[ch - 'a'] != null;
    }

    public TrieNode get(char ch) {
      return children[ch - 'a'];
    }
  }

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */

}
