package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

import leetcode.common.TreeNode;

/**
 * @author ytjia created on 2017-09-10 21:47
 */
public class SerializeandDeserializeBinaryTree {

  /**
   * Serialization is the process of converting a data structure or object into a sequence of bits
   * so that it can be stored in a file or memory buffer, or transmitted across a network connection
   * link to be reconstructed later in the same or another computer environment.
   * <p>
   * Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how
   * your serialization/deserialization algorithm should work. You just need to ensure that a binary
   * tree can be serialized to a string and this string can be deserialized to the original tree
   * structure.
   * <p>
   * https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
   */
  public class Codec {

    private static final String splitter = ",";
    private static final String NN = "null";

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
      Queue<TreeNode> nodesToProcess = new LinkedList<>();
      List<String> nodesList = new ArrayList<>();

      if (root == null) {
        nodesList.add(NN);
      } else {
        nodesToProcess.add(root);
        List<String> nodesBuffer = new ArrayList<>();
        while (!nodesToProcess.isEmpty()) {
          TreeNode nodeToProcess = nodesToProcess.poll();
          if (nodeToProcess != null) {
            nodesBuffer.add(Integer.toString(nodeToProcess.val));
            nodesList.addAll(nodesBuffer);
            nodesBuffer.clear();
            nodesToProcess.add(nodeToProcess.left);
            nodesToProcess.add(nodeToProcess.right);
          } else {
            nodesBuffer.add(NN);
          }
        }
      }

      return String.join(splitter, nodesList);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
      if (data == null || data.length() == 0) {
        return null;
      }
      List<String> nodesList = Arrays.asList(data.split(splitter));
      if (nodesList.get(0).equals(NN)) {
        return null;
      }
      Queue<TreeNode> nodesToProcess = new LinkedList<>();
      TreeNode root = new TreeNode(Integer.parseInt(nodesList.get(0)));
      boolean isLeft = true;
      TreeNode nodeToProcess = root;
      for (int i = 1; i < nodesList.size(); i++) {
        if (isLeft) {
          if (!nodesList.get(i).equals(NN)) {
            TreeNode curNode = new TreeNode(Integer.parseInt(nodesList.get(i)));
            nodeToProcess.left = curNode;
            nodesToProcess.add(curNode);
          }
        } else {
          if (!nodesList.get(i).equals(NN)) {
            TreeNode curNode = new TreeNode(Integer.parseInt(nodesList.get(i)));
            nodeToProcess.right = curNode;
            nodesToProcess.add(curNode);
          }
          nodeToProcess = nodesToProcess.poll();
        }
        isLeft = !isLeft;
      }

      return root;
    }
  }

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));

}
