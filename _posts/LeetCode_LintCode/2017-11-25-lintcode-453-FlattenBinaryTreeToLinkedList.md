---
layout: post
title:  "lintcode 453 - Flatten Binary Tree To Linked List"
date:   2017-11-25 19:24:10.684111
categories: lintcode, Snapchat
---

# Flatten Binary Tree To Linked List

## 一刷

### 代码

自己写的recursion版本，使用带返回值helper
```java
/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */


public class Solution {
    /*
     * @param root: a TreeNode, the root of the binary tree
     * @return: 
     */
    public void flatten(TreeNode root) {
        // write your code here
        flattenHelper(root);
    }
    
    private TreeNode flattenHelper(TreeNode root){
        if(root == null){
            return null;
        }
        
        TreeNode left = flattenHelper(root.left);
        TreeNode right = flattenHelper(root.right);
        
        root.left = null;
        root.right = left;
        TreeNode current = root;
        while(current.right != null){//调整后的右子树已经是一个list了，所以走到尽头再粘上左子树就可以了
            current = current.right;
        }
        
        current.right = right;
        return root;
    }
}
```

其实根本就不需要返回值也能recursion的版本
```java
/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */

public class Solution {
    /*
     * @param root: a TreeNode, the root of the binary tree
     * @return: 
     */
    public void flatten(TreeNode root) {
        // write your code here
        if(root == null){
            return;
        }
        
        flatten(root.left);
        flatten(root.right);
        
        TreeNode temp = root.right;
        root.right = root.left;
        root.left = null;
        
        while(root.right != null){
            root = root.right;
        }
        
        root.right = temp;
        
    }
}
```

iterative版本 来自[leetcode discuss - Accepted simple Java solution , iterative](https://discuss.leetcode.com/topic/5783/accepted-simple-java-solution-iterative)
```java
/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */


public class Solution {
    /*
     * @param root: a TreeNode, the root of the binary tree
     * @return: 
     */
    public void flatten(TreeNode root) {
        // write your code here
        if(root == null){
            return;
        }
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        
        while(!stack.isEmpty()){
            //将栈顶元素取出，该元素作为需要改造左右子树的元素
            TreeNode current = stack.pop();
            
            //以下这三个操作都需要if语句，因为每个都是独立的，对于不同的节点，各种情况的组合都有可能
            if(current.right != null){
                stack.push(current.right);
            }
            if(current.left != null){
                stack.push(current.left);
            }
            if(!stack.isEmpty()){
                current.right = stack.peek();
            }
            current.left = null;//很容易遗忘的一点
        }
        
    }
}
```

### 笔记

一开始感觉这题没什么头绪，因为既要遍历又要修改树的结构。但是看到了Grandyang的一句话后忽然想到了什么:

[Grandyang - Flatten Binary Tree to Linked List 将二叉树展开成链表](http://www.cnblogs.com/grandyang/p/4293853.html)
```
...只要是数的遍历就有递归和非递归的两种方法来求解，这里我们也用两种方法来求解。...
```

于是想到了一棵树的所有修改肯定是不可能一次性让一段代码修改完成的。所以肯定是**可以利用分治的思想，把树分成当前node和左子树和右子树，把左子树和右子树看成一个整体，只进行三个node之间的调整。调整完成后，再递归地对左子树和右子树进行同样的调整**。

于是就写出了自己的第一个版本，recursion，但是因为需要返回调整后的root，所以需要一个helper方法。

看了leetcode的版本后发现，其实不需要返回值也是可以直接调整的，于是就有了版本2.

对于版本1和版本2，使用recursion，思维上相对来说都还是比较直接的。而该题的iteration版本虽然可以做，但是思路需要在纸上画一下才能理清。而本题又不需要像某些题，如"Kth Smallest Element in an array"需要global的变量，所以个人感觉iteration的版本更好。而且iteration的版本因为需要使用stack，还会占用额外的空间。