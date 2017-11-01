---
layout: post
title:  "leetcode 669 - Trim a Binary Search Tree"
date:   2017-10-11 21:31:02.963495
categories: leetcode, Bloomberg
---

# Trim a Binary Search Tree

## 一刷

### 代码


自己写的版本，保留了原树，deep copy出新的树
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
    public TreeNode trimBST(TreeNode root, int L, int R) {
        
        if(root == null || L > R){
            return null;
        }
        
        
        TreeNode newRoot = trimBSTHelper(root, L, R);
        
        return newRoot;
        
    }
    
    private TreeNode trimBSTHelper(TreeNode from, int L, int R){
        if(from == null){
            return null;
        }
        
        if(from.val >= L && from.val <= R){
            TreeNode copyNode = new TreeNode(from.val);
            copyNode.left = trimBSTHelper(from.left, L, R);
            copyNode.right = trimBSTHelper(from.right, L, R);
            return copyNode;
        }
        
        if(from.val < L){
            return trimBSTHelper(from.right, L, R);
        }
        
        //if(from.val > R)
        return trimBSTHelper(from.left, L, R);
        
    }
}
```

leetcode版本，shallow copy，直接在原来的树的基础上进行trim
(并没有判断如果L > R的情况)
```java
class Solution {
    public TreeNode trimBST(TreeNode root, int L, int R) {
        if (root == null) return root;
        if (root.val > R) return trimBST(root.left, L, R);
        if (root.val < L) return trimBST(root.right, L, R);

        root.left = trimBST(root.left, L, R);
        root.right = trimBST(root.right, L, R);
        return root;
    }
}
```

### 笔记

一开始一度以为没有思路，写不下去。但是稍微想了想，然后忽然豁然开朗，一遍通过。

首先，一开始毫无疑问的可以从例子中看出来，对于树中的某个node：
1. 如果这个node自己的值小于L，说明只有右子树中的nodes中会存在满足区间的点(并不保证有，更不保证所有都是)。所以左子树和该node自己就完全可以被剪枝剪掉。
2. 如果这个node自己的值大于R，说明只有左子树中的nodes中会存在满足区间的点(并不保证有，更不保证所有都是)。所以右子树和该node自己就完全可以被剪枝剪掉。
3. 如果这个node处于区间之中，则保留这个node，然后再进一步对左右子树进行递归判断。

从上面的思路上可以大概感觉出来应该是divide and conquer没跑。但是具体实现的思路上有点混乱，疑惑如果当前点被减掉，到底该怎么表示？

其实很简单，当前点如果不保留则直接返回递归子树的结果。而如果当前子树保留，则先左右分别递归，**再合并**，然后返回当前结果(因为此时所有子递归已经完成)。

最后注意，如果不进行deep copy，Leetcode solution中的解决方案和自己的有什么区别。