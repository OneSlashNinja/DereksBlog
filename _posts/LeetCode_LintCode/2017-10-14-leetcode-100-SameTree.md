---
layout: post
title:  "leetcode 100 - SameTree"
date:   2017-10-14 11:39:24.538823
categories: leetcode, Bloomberg
---

# SameTree

## 一刷

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
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        
        if(p == null && q == null){
            return true;
        }
        
        if(p == null && q != null || p != null && q == null){
            return false;
        }
        
        if(p.val != q.val){
            return false;
        }
        
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
        
    }
}
```

### 笔记

一遍过。

其实应该先做这题再做101 Symmetric Tree。这题完全就是Symmetric Tree的前戏。Symmetric相当于把本题作为一个helper方法进行调用即可。