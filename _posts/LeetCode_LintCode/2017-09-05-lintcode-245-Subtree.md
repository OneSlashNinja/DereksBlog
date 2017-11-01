---
layout: post
title:  "lintcode 245 - Subtree"
date:   2017-09-05 21:26:00.800458
categories: lintcode, Google, BinaryTree, Recursion
---

# Subtree

## 一刷

### 代码

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
     * @param T1: The roots of binary tree T1.
     * @param T2: The roots of binary tree T2.
     * @return: True if T2 is a subtree of T1, or false.
     */
    private boolean isIdenticalTree(TreeNode T1, TreeNode T2){
        
        //T1 == T2 == null NOT working
        if(T1 == null && T2 == null){
            return true;
        }
        
        if(T1 == null || T2 == null || T1.val != T2.val){
            return false;
        }
        
        return (isIdenticalTree(T1.left, T2.left) && isIdenticalTree(T1.right, T2.right));
        
    }
    
    public boolean isSubtree(TreeNode T1, TreeNode T2) {
        // write your code here
        
        if(isIdenticalTree(T1, T2)){
            return true;
        }
        
        //注意这里如果不判断T1 == null则当T1为null的时候会出现NullPointer的错误
        //而只判断T1 == null，并且返回false，因为(T1 == null && T2 == null)的情况其实在前面isIdenticalTree中已经判断过了
        if(T1 == null){
            return false;
        }
        
        return (isSubtree(T1.left, T2) || isSubtree(T1.right, T2));
        
    }
}
```

### 笔记

感觉这题主要考察的就是利用recursion的tree的divide and conquer。

另外这种类型的题目对于TreeNode为null的情况的判断需要额外注意。