---
layout: post
title:  "leetcode 156 - Binary Tree Upside Down"
date:   2017-07-23 23:16:18.139069
categories: leetcode, Linkedin
---

# Binary Tree Upside Down

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
public class Solution {
    public TreeNode upsideDownBinaryTree(TreeNode root) {
        
        if(root == null || root.left == null){
            return root;
        }
        
        TreeNode newRoot = upsideDownBinaryTree(root.left);
        
        root.left.left = root.right;
        root.left.right = root;
        root.left = null;
        root.right = null;
        
        return newRoot;
    }
}
```

### 笔记

这题是一道非常奇葩的题目，不太像其他的binary tree的题目，不过从这题中倒是领悟了蛮多技巧和知识。

这题一开始完全没什么思路和概念，看了leetcode discuss后发现其实大家都一样。写出那个非常棒解释的仁兄也是看了好半天才明白。

把当前的树想象成一个梳子，从根到最左下角的这一溜可以看成是梳子的bone，从bone上伸出去的部分可以看成是teeth。那么要做的其实就是错开teeth。


看了recursion的版本发现了这么几个重要的发现:

1. 
其实二叉树的甚至是任何使用recursion的函数都遵守这么一个规律:

**以recursion的调用作为分界线, 在其上的代码遵循自顶向下的过程，在其下的则是遵循自底向上的过程**

比如这题

        root.left.left = root.right;
        root.left.right = root;
        root.left = null;
        root.right = null;

这个反转的过程就是从底向上的，这样，向上的过程会有记忆，所以不用担心反转了root会递归不回去。

2. 

这题和binary tree的分治法型的题目处理的区别：

(1) 首先，分治法往往是关心左右两边返回的结果，而这题只关心最左边哪一个分支的情况

(2) 更重要的一个区别，分治法往往是在左右两边都返回结果之后，根据两边的结果做一些加工操作，然后把整合的结果作为向上传递的结果return回去。而这题不一样，这题只需要把最左边的那个叶子节点找到后，作为最终的root而蹭蹭传递上去。所以可以发现
```java
        TreeNode newRoot = upsideDownBinaryTree(root.left);
        
        root.left.left = root.right;
        root.left.right = root;
        root.left = null;
        root.right = null;
        
        return newRoot;
```

recursion到return之间，完全没有任何操作碰newRoot，返回的结果也是和这些操作没有任何关系。

3. 

触底条件仍然需要放在在前头。

并且观察该题的触底条件，会发现和普通的分治有不同，普通的分治一般只有:

`if(root == null){return null;}`

但是这题的触底条件是
```java
if(root == null || root.left == null){
    return root;
}
```

也就使得recursion到最左叶子就停止，而不会继续到最左叶子节点的为null的left。这对返回真正的最左叶子节点作为新的根节点非常重要。

此题还有iteration迭代的版本，在此略过。