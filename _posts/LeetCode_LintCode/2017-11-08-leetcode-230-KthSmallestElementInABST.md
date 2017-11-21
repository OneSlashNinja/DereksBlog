---
layout: post
title:  "leetcode 230 - KthSmallestElementInABST"
date:   2017-11-08 21:48:31.713954
categories: leetcode, Google,Bloomberg,Uber
---

# KthSmallestElementInABST

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
    public int kthSmallest(TreeNode root, int k) {
        
        if(root == null){
            throw new IllegalArgumentException();
        }
        
        Stack<TreeNode> stack = new Stack<>();
        
        while(root != null || !stack.isEmpty()){
            if(root != null){
                stack.push(root);
                root = root.left;
            }else{
                root = stack.pop();
                //每弹一次就统计一次
                k--;
                if(k == 0){
                    //这里也可以直接return，但是break后处理起来比较好看？
                    break;
                }
                root = root.right;
            }
        }
        
        return root.val;
    }
}
```

### 笔记

这题就是一道非常经典的对于BST，只能使用iterative，而没法使用recursive的题。

因为这道题的限定是第k小，而使用recursive的divide and conquer并不能胜任，因为就像国王给两个老臣分配任务，而两个老臣又给两个下属分配任务，这样每个人之间没法知道互相的进度。所以需要一个**全局变量**。而iterative因为不会递归，所以可以将该变量维护在函数中。

这题基本思路就是: 因为inorder traverse是按顺序的，所以inorder走到第k个就是第k小的元素了

的最精妙的就是直接使用k--，当k为0时，就说明走到了该元素了。

本题几乎和inorder traverse binary tree的版本一模一样，唯一添加了就是当弹一个元素的时候就k--，当k减少到0的时候就说明找到了。