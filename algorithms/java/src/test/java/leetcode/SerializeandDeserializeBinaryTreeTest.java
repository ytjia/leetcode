package leetcode;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import leetcode.common.TreeNode;

/**
 * @author ytjia created on 2017-09-11 11:54
 */
public class SerializeandDeserializeBinaryTreeTest {

  private SerializeandDeserializeBinaryTree.Codec codec;
  TreeNode root = new TreeNode(1);
  TreeNode node2 = new TreeNode(2);

  @Before
  public void setUp() throws Exception {
    SerializeandDeserializeBinaryTree serializeandDeserializeBinaryTree =
        new SerializeandDeserializeBinaryTree();
    codec = serializeandDeserializeBinaryTree.new Codec();
    root.right = node2;
  }

  @Test
  public void testSerialize() throws Exception {
    Assert.assertEquals("1,null,2", codec.serialize(root));
  }

  @Test
  public void testDeserialize() throws Exception {
    Assert.assertEquals("1,null,2", codec.serialize(codec.deserialize("1,null,2")));
    Assert.assertEquals("1,2", codec.serialize(codec.deserialize("1,2")));

  }
}
