---
layout: post
title:  "leetcode 101 - SymmetricTree"
date:   2017-10-11 23:38:10.877359
categories: leetcode, Bloomberg
---

# Symmetric Tree

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
    public boolean isSymmetric(TreeNode root) {
        
        if(root == null){
            return true;
        }
        
        return compare(root.left, root.right);
        
    }
    
    private boolean compare(TreeNode left, TreeNode right){
        
        if(left == null && right == null){
            return true;
        }
        
        if(left == null || right == null){
            return false;
        }
        
        //the filter upper can make sure when code comes here, left != null && right != null
        if(left.val != right.val){
            return false;
        }
        
        //the filter upper can make sure when code comes here, left.val == right.val
        return compare(left.left, right.right) && compare(left.right, right.left);
        
    }
    
}
```

### 笔记

也是一开始感觉应该是可以用递归，但是思路很混乱，感觉自己做不出来。但是静下来想一想就想通了，一遍过。

重点在于，symmetric的特点是只针对于整个树的root，每个子树并能**单独**地去递归检测是否符合symmetric的特性。

所以可以想到，该递归的参数应该是两个参数，代表同一层镜像位置的两个node。然后比较的时候:

1. 先进行是否null的filter:

```java
if(left == null && right == null){
    return true;
}

if(left == null || right == null){
    return false;
}
```

2. 过滤完了第一层就可以保证至少可以取两者的val了。那么如果val相当则还是有可能镜像的，如果不同，则肯定不镜像

3. 然后再镜像地进行递归: left.right和right.left比较，left.left和right.right进行比较。aggregate返回的结果，再进行返回。

