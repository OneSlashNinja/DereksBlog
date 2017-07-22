---
layout: post
title:  "LeetCode 235 - Lowest Common Ancestor of a Binary Search Tree"
date:   2017-07-16 00:15:02 -0400
categories: leetcode, Microsoft
---

# Lowest Common Ancestor of a Binary Search Tree

## 一刷

### 代码

recursion版本
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
public class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        
        //不写这一项仍然会通过，不过如果出现p和q都不在树中的情况，最好还是写上这一项
        if(root == null){
            return null;
        }
        
        //注意是>而不是>=,因为等于的情况就会导致该root就应该是ancestor
        if(root.val > p.val && root.val > q.val){
            return lowestCommonAncestor(root.left, p, q);
        }
        
        if(root.val < p.val && root.val < q.val){
            return lowestCommonAncestor(root.right, p, q);
        }
        
        return root;
    }
}
```

看过leetcode discuss后自己写的iteration的版本
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
public class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        
        //root != null一样也是安全性的检查，不写也能通过，不过忽略了p和q不在树中的情况
        while(root != null && (root.val - p.val) * (root.val - q.val) > 0){
            if(root.val > p.val){
                root = root.left;
            }else{
                root = root.right;
            }
        }
        
        return root;
    }
}
```


### 笔记

这一题是和Lowest Common Ancestor of A Binary Tree最好的比较。

因为是BST，所以left.val < root.val < right.val是最好的可以利用的条件。

当p和q的值都大于或者小于(注意没有等于)root的值时，说明当前root是common ancestor，但不是Lowest common ancestor。Lowest one应该在p和共同在的那一侧，所以应该继续往深里搜索。

这题也是一个非常好的比较递归和递推实现的例子。

自己的写法是递归式的写法。看了leetcode discuss后的递推版本发现更加简洁。利用了"在同一侧的子树中" == "相减的结果相乘一定 < 0"的这个条件，非常巧妙。


