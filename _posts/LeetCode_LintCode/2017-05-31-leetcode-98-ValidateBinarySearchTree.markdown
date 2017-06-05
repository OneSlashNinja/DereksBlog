---
layout: post
title:  "LeetCode 98 - Validate Binary Search Tree"
date:   2017-05-31 00:22:02 -0400
categories: leetcode, Amazon
---

# Validate Binary Search Tree

## 一刷

### 代码
自己的版本(divide and conquer):
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
class ResultType{
    public int maxVal;
    public int minVal;
    public boolean isValid;
    public ResultType(int maxVal, int minVal, boolean isValid){
        this.maxVal = maxVal;
        this.minVal = minVal;
        this.isValid = isValid;
    }
}
 
public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: True if the binary tree is BST, or false
     */
     
     
    
    public boolean isValidBST(TreeNode root) {
        // write your code here
        return validateBSTHelper(root).isValid;
    }
    
    public ResultType validateBSTHelper(TreeNode root){
        
        if(root == null){
            return new ResultType(Integer.MIN_VALUE,Integer.MAX_VALUE,  true);
        }
        
        ResultType leftResult = validateBSTHelper(root.left);
        ResultType rightResult = validateBSTHelper(root.right);
        
        boolean isCurrentRootBSTValid;
        
        if(root.left != null && leftResult.maxVal >= root.val){
            isCurrentRootBSTValid = false;
        }else if(root.right != null && rightResult.minVal <= root.val){
            isCurrentRootBSTValid = false;
        }else{
            isCurrentRootBSTValid = true;
        }
        
        ResultType returnResult = new ResultType(Math.max(Math.max(leftResult.maxVal, rightResult.maxVal), root.val), Math.min(Math.min(leftResult.minVal, rightResult.minVal), root.val), leftResult.isValid && rightResult.isValid && isCurrentRootBSTValid);
                                                
        return returnResult;
    }
}
```

### 笔记
思维上的错误：
(1)觉得左右两边都应该取maximum进行比较。其实要保证左子树中所有node比root小就应该是保证左子树中最大的数都比root的小，而要保证右子树中中所有node都比root大则是要保证右子树中最小的数都比root大，所以ResultType需要一个maxVal需要一个minVal。
(2)对root为null时返回的ResultType进行赋值时，maxVal直接赋Integer.MAX_VALUE。而minVal直接赋Integer.MIN_VALUE。其实应该是相反的。

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
public class Solution {
    
    class Tracker{
        public int maxValue;
        public int minValue;
        public boolean isValid;
        
        public Tracker(int maxValue, int minValue, boolean isValid){
            this.maxValue = maxValue;
            this.minValue = minValue;
            this.isValid = isValid;
        }
    }

    public boolean isValidBST(TreeNode root) {
        return divideAndConquerHelper(root).isValid;
    }
    
    private Tracker divideAndConquerHelper(TreeNode root){
        if(root == null){
            return new Tracker(Integer.MIN_VALUE, Integer.MAX_VALUE, true);
        }
        
        Tracker leftResult = divideAndConquerHelper(root.left);
        Tracker rightResult = divideAndConquerHelper(root.right);
        
        if(!leftResult.isValid || !rightResult.isValid){
            return new Tracker(Integer.MIN_VALUE, Integer.MAX_VALUE, false);
        }
        
        //这里的比较需要注意两点:
        //(1)需要注意leftResult.maxValue >= root.val和rightResult.minValue <= root.val要有=,因为题目中规定了不能相等
        //(2)需要将root.left和root.right和null进行比较。这是因为，
        //如果root.left == null的话，返回回来的tracker的maxValue和minValue就会变成Integer.MIN_VALUE, Integer.MAX_VALUE
        //这样的话，如果当前root.val的值和其中某一个相等，那么就会被判定为isValid为false
        if((root.left != null && leftResult.maxValue >= root.val) || (root.right != null && rightResult.minValue <= root.val)){
            return new Tracker(Integer.MIN_VALUE, Integer.MAX_VALUE, false);
        };
        
        return new Tracker(Math.max(Math.max(leftResult.maxValue, rightResult.maxValue), root.val),
                            Math.min(Math.min(leftResult.minValue, rightResult.minValue), root.val),
                            true);
    }
}
```


### 笔记
实现的思路还是比较清晰的，**利用divide and conquer， 配合一个额外的返回类型来包装所有需要的信息**

二刷的时候发现在判断最后一个是否valid的环节上，需要有两点的注意，具体的见注释。

另外leetcode中有一个不用借助额外的变量，使用iterative inorder traverse的版本非常巧妙并且精简。

而且更值得一提的是该作者是总结除了这种使用这种巧妙使用stack来达到非递归的inorder traverse的框架或者模板，针对三道题都可以使用该模板：

最基本的**Binary Tree Inorder Traversal**,这可以说是基础模板

还有**Kth Smallest Element in a BST**
还有这道**Validate Binary Search Tree**

<https://discuss.leetcode.com/topic/46016/learn-one-iterative-inorder-traversal-apply-it-to-multiple-tree-questions-java-solution>