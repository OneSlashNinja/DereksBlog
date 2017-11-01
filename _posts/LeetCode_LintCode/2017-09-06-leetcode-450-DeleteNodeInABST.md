---
layout: post
title:  "leetcode 450 - Delete Node In a BST"
date:   2017-09-06 21:44:58.966569
categories: leetcode, Uber, Microsoft
---

# Delete Node In a BST

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
    public TreeNode deleteNode(TreeNode root, int key) {
                // write your code here
        
        if(root == null){
            return null;
        }
        
        if(root.val < key){
            root.right = deleteNode(root.right, key);
        }else if(root.val > key){
            root.left = deleteNode(root.left, key);
        }else{
            if(root.left == null){
                return root.right;
            }else if(root.right == null){
                return root.left;
            }else{
                TreeNode rightMin = findRightMin(root.right);
                root.val = rightMin.val; //并不是真正的删除了该节点，而是相当于替换了value，然后删除被替换的节点
                root.right = deleteNode(root.right, rightMin.val);//not root.right = removeNode(root, rightMin.val);
            }
        }
        
        return root;
    }
    
    private TreeNode findRightMin(TreeNode root){
        
        while(root.left != null){
            root = root.left;
        }
        return root;
    }
}
```

### 笔记

这道题一开始没什么头绪，看解答才发现明白了思路其实没有想象中的那么难。这题在lintcode上叫**Remove Node in Binary Search Tree**。

这题最主要要注意的就是: **分步骤，分情况**，并且code也是非常好体现了这一点

首先，分步骤。从步骤上来讲分两步:

1. 搜索key在树中的位置

2. 找到后，进行删除

而第二步看似很复杂，没有什么规律可寻，但分多种不同情况之后就会很清晰:

1. 如果左子树和右子树都为空那么说明要删除的是叶子节点，直接删除即可。

2. 如果左子树或者右子树中中有一个为空，那么删除节点后把剩余的那个子树直接“接上”即可。

3. 如果左子树和右子树都不为空，那么有两种策略: 选择左子树中最大的那个node，或者选择右子树中最小的那个node补上即可(整个算法都选择一种策略就行，并且这里需要注意:**这左子树中最大的node和找右子树中最小的node并不是找successor或者predecessor，successor和predecessor是找整个树中第一个比该元素大或者小的元素，是有可能在parent中的**)。

整个程序的if结构也是按照上面的分析展开的: 外层的if配合recursion是用来进行搜索的，内层的if配合recursion是具体进行删除的，判断不同的情况。

单独的findRightMin拿出来作为一个method。


注意，此题到底什么时候返回，什么时候是需要将返回的结果赋值有点容易混淆或者搞错，规律是所有递归调用函数自己的地方都需要去**接住返回的结果**

[Leetcode - Recursive Easy to Understand Java Solution](https://discuss.leetcode.com/topic/65792/recursive-easy-to-understand-java-solution)
[Grandyang - Delete Node in a BST 删除二叉搜索树中的节点](http://www.cnblogs.com/grandyang/p/6228252.html)