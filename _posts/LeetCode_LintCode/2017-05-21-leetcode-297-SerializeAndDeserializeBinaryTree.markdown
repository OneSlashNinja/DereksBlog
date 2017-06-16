---
layout: post
title:  "LeetCode # - Serialize and Deserialize Binary Tree"
date:   2017-05-21 00:18:02 -0400
categories: leetcode, Amazon
---

# Serialize and Deserialize Binary Tree

## 一刷

### 代码
```java

```

### 笔记


---

## 二刷

### 代码

使用stack版本
```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        serializeHelper(root, sb);
        return sb.toString();
    }
    
    private void serializeHelper(TreeNode root, StringBuilder sb){
        
        if(root == null){
            sb.append("#,");
            return;
        }
        
        sb.append(root.val);
        sb.append(',');
        serializeHelper(root.left, sb);
        serializeHelper(root.right, sb);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] splitedData = data.split(",");
        Stack<String> stack = new Stack<String>();
        for(int i = splitedData.length - 1; i >= 0; i--){
            stack.push(splitedData[i]);
        }
        
        return deserializeHelper(stack);
    }
    
    private TreeNode deserializeHelper(Stack<String> stack){
        //其实不用写这一步，如果真的出现了stack.isEmpty()说明出错了，因为所有的根节点会在遇到'#'的时候就停止继续recursion
        //if(stack.isEmpty()){
        //    return null;
        //}
        
        String popedVal = stack.pop();
        
        if(popedVal.equals("#")){
            return null;
        }
        
        TreeNode root = new TreeNode(Integer.parseInt(popedVal));
        root.left = deserializeHelper(stack);
        root.right = deserializeHelper(stack);
        
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));
```

使用int[]来当int指针版本

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        
        if(root == null){
            return "";
        }

        StringBuilder sb = new StringBuilder();

        serializeHelper(root, sb);
        //下面这句可以不要，因为split如果逗号在最后会直接把后面的部分忽略。
        //另外要注意的是StringBuilder的长度是length(),和String一样，不是size。size是容器的。
        //StringBuilder的删除是deleteCharAt()
        //sb.deleteCharAt(sb.length() - 1);

        return sb.toString();

    }

    //虽然同样都是divide and conquer, serialize因为StringBuilder作为收集自底向上的容器，所以的返回参数是void
    //但deserialize的参数是TreeNode，这个TreeNode是作为容器的
    private void serializeHelper(TreeNode root, StringBuilder sb){

        if(root == null){
            //注意逗号要和后面的顺序一致，下面用的是先value后"," 所以这里不能写成sb.append(",#");
            sb.append("#,");
            //这是触底条件，要记得return
            return;
        }

        sb.append(root.val);
        sb.append(",");
        serializeHelper(root.left, sb);
        serializeHelper(root.right,sb);

    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] dataArr = data.split(",");
        int[] index = {0};

        deserializeHelper(dataArr);
    }

    private TreeNode deserializeHelper(String[] data, int[] index){

        if(data[index[0]].equals("#")){
            return null;
        }

        TreeNode root = new TreeNode(data[index[0]].val);
        root.left = deserializeHelper(data, ++index[0]);
        root.right = deserializeHelper(data, ++index[0]);

        return TreeNode;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));
```

### 笔记
