---
layout: post
title:  "leetcode 366 - Find Leaves Of Binary Tree"
date:   2017-07-19 19:30:26.902699
categories: leetcode, Linkedin
---

# Find Leaves Of Binary Tree

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
    public List<List<Integer>> findLeaves(TreeNode root) {
        
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        
        findLeavesHelper(root, results);
        
        return results;
        
    }
    
    private int findLeavesHelper(TreeNode root, List<List<Integer>> results){
        
        if(root == null){
            return 0;
        }
        
        int leftDepth = findLeavesHelper(root.left, results);
        int rightDepth = findLeavesHelper(root.right, results);
        
        int currentDepth = Math.max(leftDepth, rightDepth) + 1;
        
        while(results.size() < currentDepth){
            results.add(new ArrayList<Integer>());
        }
        
        results.get(currentDepth - 1).add(root.val);
        
        return currentDepth;
    }
    
}
```

### 笔记

关键点是要能够把**在哪一个list中和具体某个node所对应的depth**对应起来。

一开始感觉应该是recursion，然后自底向上的过程中开始输出，这样的话肯定能保证输出的顺序是按要求的。但是并不能知道层级信息。然后看到提示说其实层级就是树的depth，一下就豁然开朗了。
