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


### 笔记
