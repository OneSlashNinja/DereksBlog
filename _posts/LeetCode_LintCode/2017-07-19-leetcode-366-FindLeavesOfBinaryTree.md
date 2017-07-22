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


