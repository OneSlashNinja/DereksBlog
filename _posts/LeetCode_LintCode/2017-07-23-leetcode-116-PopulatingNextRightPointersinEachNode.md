---
layout: post
title:  "leetcode 116 - Populating Next Right Pointers in Each Node"
date:   2017-07-23 11:49:00.632937
categories: leetcode, Microsoft
---

# Populating Next Right Pointers in Each Node

## 一刷

### 代码

```java
/**
 * Definition for binary tree with next pointer.
 * public class TreeLinkNode {
 *     int val;
 *     TreeLinkNode left, right, next;
 *     TreeLinkNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void connect(TreeLinkNode root) {
        
        Queue<TreeLinkNode> queue = new LinkedList<>();
        
        if(root == null){
            return;
        }
        
        queue.offer(root);
        
        while(!queue.isEmpty()){
            int size = queue.size();
            
            for(int i = 0; i < size; i++){
                TreeLinkNode current = queue.poll();
                if(i != size - 1){
                    TreeLinkNode neighbor = queue.peek();
                    current.next = neighbor;
                }
                
                if(current.left != null ){
                    queue.offer(current.left);
                }
                if(current.right != null){
                    queue.offer(current.right);
                }
            }
            
        }
        
    }
}
```

### 笔记

看到题目中的example:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL

时想到了什么?

这不完全就是level order traverse么?

直接BFS加level信息就搞定了。

不过相比leetcode discuss中的recursion的版本，BFS的版本时间复杂度是O(n)没什么好优化的，但是空间复杂度是O(n),则相比recursion的版本稍微差一些了。

不过个人感觉该版本易懂，适用性广，而且不用改任何代码就能直接解决Populating Next Right Pointers in Each Node 2.

要注意如何防止queue中有null被存入，基本原则就是**对所有会产生offer的地方都进行检测**：

在初始压入第一个元素root的时候对root进行检测。在压入current的left和right的时候对这两个元素也进行检测。