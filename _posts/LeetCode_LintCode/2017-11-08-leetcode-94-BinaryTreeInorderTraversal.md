---
layout: post
title:  "leetcode 94 - BinaryTreeInorderTraversal"
date:   2017-11-08 20:59:49.192361
categories: leetcode, Microsoft
---

# BinaryTreeInorderTraversal

## 一刷

### 代码

trivial的recursion版本
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
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        
        List<Integer> results = new ArrayList<Integer>();
        
        inorderTraversalHelper(root, results);
        
        return results;
    }
    
    private void inorderTraversalHelper(TreeNode root, List<Integer> results){
        
        if(root == null){
            return;
        }
        
        inorderTraversalHelper(root.left, results);
        results.add(root.val);
        inorderTraversalHelper(root.right, results);
        
    }
}
```

Iteratively 形式1
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
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        
        List<Integer> results = new ArrayList<Integer>();
        
        Stack<TreeNode> stack = new Stack<>();
        
        while(root != null || !stack.isEmpty()){
            
            while(root != null){
                stack.push(root);
                root = root.left;
            }
            
            root = stack.pop();
            results.add(root.val);
            root = root.right;
        }
        
        
        return results;
    }
}
```

Iteratively 形式2
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
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        
        List<Integer> results = new ArrayList<Integer>();
        
        Stack<TreeNode> stack = new Stack<>();//注意stack中存的是TreeNode而不是Integer
        
        while(root != null || !stack.isEmpty()){
            if(root != null){
                stack.push(root);
                root = root.left;
            }else{//也就是!stack.isEmpty()会落到这里
                root = stack.pop();
                results.add(root.val);//和pre order的唯一区别就是这一行的位置
                root = root.right;
            }
        }
        
        
        return results;
    }
}
```

### 笔记

recursion的版本自然是没什么说的，这题如果只能写这个版本就太low了，肯定不够。

那么iteration的版本是怎么的样的思路，关键的地方和优势呢？

关键点: **Stack**

整个过程是通过stack来完成的(注意stack中存的是TreeNode而不是Integer)，配合while循环。

第一个版本的iterative对于BinaryTreeInorderTraversal， Kth Smallest Element in a BST和 Validate Binary Search Tree的模板见:
[leetcode - BST iterative 三种模板](https://discuss.leetcode.com/topic/46016/learn-one-iterative-inorder-traversal-apply-it-to-multiple-tree-questions-java-solution)

而第二个版本的iterative感觉更好记，更好理解，并且更易拓展。

好记，是因为**只有一个while循环，并且while循环中的两个条件也就是(root != null || !stack.isEmpty())相当于会分别落入if和else中，如果root不为null，则一直向左走，如果为null，则弹出一个，并向右走一次。**

[leetcode discuss - Preorder, Inorder, and Postorder Iteratively Summarization](https://discuss.leetcode.com/topic/30632/preorder-inorder-and-postorder-iteratively-summarization)

