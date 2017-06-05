---
layout: post
title:  "LeetCode 236 - Lowest Common Ancestor of a Binary Tree"
date:   2017-05-22 00:22:02 -0400
categories: leetcode, Amazon
---

# Lowest Common Ancestor of a Binary Tree

## 一刷

### 代码
version(自己写的错误版本，错误理解题意)：
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
    /**
     * @param root: The root of the binary search tree.
     * @param A and B: two nodes in a Binary.
     * @return: Return the least common ancestor(LCA) of the two nodes.
     */
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode A, TreeNode B) {
        // write your code here
        
        if(root == null || A == null || B == null){
            return null;
        }
        
        while(root != null){
            if(root.val > A.val && root.val > B.val){
                root = root.left;
                continue;
            }
            
            if(root.val < A.val && root.val < B.val){
                root = root.right;
                continue;
            }
            
            return root;
        }
        
        return root;
    }
}
```

version(recursion版本,原版本4行代码)：
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
    /**
     * @param root: The root of the binary search tree.
     * @param A and B: two nodes in a Binary.
     * @return: Return the least common ancestor(LCA) of the two nodes.
     */
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode A, TreeNode B) {
        // write your code here
        
        if(root == null || root == A || root == B){
            return root;
        }
        
        TreeNode leftReturn = lowestCommonAncestor(root.left, A, B);
        TreeNode rightReturn = lowestCommonAncestor(root.right, A, B);

        
        if(leftReturn == null){
            return rightReturn;
        }
        
        if(rightReturn == null){
            return leftReturn;
        }
        
        return root;
    }
}
```

### 笔记

该题要吸取教训是读题，如果该题问的BST，用version1应该是没有问题的,但是题中是binary tree：
但是不管是BST还是普通binary tree，大概的思路是一致的：
如果node p和q都在root的左边，那么公共祖先肯定在左子树中。如果都在右边，就肯定都在右子树中，如果一个在左一个在右，则root自己便是公共祖先。

如果是BST，可以很方便地用p和q的val跟root的val进行比较，然后应用上面的规则即可，复杂度应该是O(h)，h是树高。
但是如果是binary tree，因为没有BST的特性，所以不能比较后“二分”地舍一半，需要用recursion使用搜索+比较的方法：
(1)在从root往下的过程是搜索的过程，触底条件是找到p或者q或者已经到底。
(2)在触底后的返回操作前只有筛选的操作：看返回的搜索结果是找到了左右都有结果还是只有一边。（这里其实还肯定会有leftReturn和rightReturn都是null的情况，那么其实会直接落入第一个if中而返回null）。
再返回过程中相当于：
如果p和q都没搜索到，那么返回null，
如果p和q搜索到了一个，那么就会把其中这一个像bubble up一样一直返回，直到，某个root，左边找打一个，右边找到一个，那么自此开始就会一直把root开始bubble up。（因为，root开始再往上，肯定另一边每次都是null）。

这题还有一点要注意的是if(root == null || root == A || root == B)而不是比较root和A的val

虽然程序短，不过相比于如果是BST的情况，因为是搜索，所以可能会遍历整个tree一遍，所以复杂度会高，应该是O(n)的



后续补充，其实这题虽然短，但其实node可能的状态还是比较复杂的：
比如下面这棵树，如果要找6和0的公共祖先

                 _______10________
                /                 \
        _______3______             9
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4

那么node可能会在如下状态中：
(0)自己就是要找的点之一，返回自己。(为什么？这样并不能确定返回的就是最小公共祖先啊，并且再往深的元素都不管了？这就需要分情况讨论：
<1>如果两个node在同一条发散自root来的path上，比如5和2，那么走到5时就不会再往深里走了，这样导致的结果就是从其他任何一点都不会再返回其他node，所以5最终会"冒泡到"root10上。
<2>如果两个node不在同一条发散自root的path上，比如5和1，那么走到5时再往深里也没有探索的必要了。而在往回冒泡的过程中两者会相遇在3，这样就能确定3是最小公共祖先了。)

(1)左子树和右子树中都没有任何要找的节点，比如2。这样的话，从7和4都会返回null，自己也会返回null。
(2)左子树中或者右子树中只有一个要找的点，比如1。这样的话，0会返回0，自己也会返回0.
(3)左子树和右子树分别有一个要找的点，比如3。这样的话，自己就是最小公共祖先。所以返回自己3.
(4)左子树或者右子树中有两个要找的点，比如10.这样的话，自己是公共祖先，但不是最小公共祖先，所以返回包含两个点的传递回来的结果3.

其中(0)(2)(3)(4)都被显式地覆盖了，而(1)虽然程序里没有写出来，但也是被隐式地覆盖了。

这算是一个有3种"触底"情况，也会根据子问题的结果有3种不同返回的题。很短但是很巧妙。

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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        
        if(root == null || root == p || root == q){
            return root;
        }
        
        TreeNode leftReturn = lowestCommonAncestor(root.left, p, q);
        TreeNode rightReturn = lowestCommonAncestor(root.right, p, q);
        
        //if(leftReturn == null && rightReturn == null){return null;}
        
        if(leftReturn == null){
            return rightReturn;
        }
        
        if(rightReturn == null){
            return leftReturn;
        }
        
        //if(rightReturn != null && leftReturn != null)
        return root;
        
    }
}
```


### 笔记

这题而一刷的时候的笔记已经写的非常详细了，但二刷的时候愣是没想起来思路是怎么样的。感觉应该是利用分治法的"撒网"和"收网"太过精妙和巧妙，一时没想起来。

首先这道题目的最核心的解题点在于：**如果node p和q都在root的左边，那么公共祖先肯定在左子树中。如果都在右边，就肯定都在右子树中，如果一个在左一个在右，则root自己便是公共祖先。**

明白这点之后，再配合**分治法**的思路(**自顶往下的过程为搜索，自底向上的过程为筛选**)和框架，在一开始判断root是否为空或者要找的目标，如果是，就说明已经"触底"，需要开始return返回。
如果没有触底，那么就进行分治，对于二叉树也就是对左子树和右子树继续进行recursion。
当手机到了来自左子树和右子树的结果后，分情况进行返回。
根据左子树和右子树返回来的的结果是否为null有4种组合，只不过有一些四种情况中的两者都为空的情况不写出来也会被涵盖。return root的其实经过前面的if的过滤也可以不需要if的判断。