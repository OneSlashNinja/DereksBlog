---
layout: post
title:  "lintcode 651 - Binary Tree Vertical Order Traversal"
date:   2017-11-24 22:49:49.936021
categories: lintcode, Facebook,Google,Snapchat
---

# Binary Tree Vertical Order Traversal

## 一刷

### 代码

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
    /*
     * @param root: the root of tree
     * @return: the vertical order traversal
     */
    public List<List<Integer>> verticalOrder(TreeNode root) {
        // write your code here
        
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        
        if(root == null){
            return results;
        }
        
        HashMap<Integer, List<Integer>> colMap = new HashMap<>();
        
        //nodeQueue和colNumQueue中的元素都是对应的，其实可以使用额外的一个Pair类来代替，不过简单起见，可以使用两个queue
        //一个代表当前Node元素的queue，一个代表对应的node元素所在的列数
        Queue<TreeNode> nodeQueue = new LinkedList<>();
        Queue<Integer> colNumQueue = new LinkedList<>();
        
        nodeQueue.offer(root);
        colNumQueue.offer(0);
        
        //为了确定colMap中key的上限和下限，也就是最后一遍循环的范围
        int colMin = 0;
        int colMax = 0;
        
        //其实就是拓展的BFS
        while(!nodeQueue.isEmpty()){
            
            //因为不涉及level order，所以不需要提前先提取出queue的size
            TreeNode current = nodeQueue.poll();
            int colNum = colNumQueue.poll();
            
            //on the fly地对min和max进行更新
            colMin = Math.min(colMin, colNum);
            colMax = Math.max(colMax, colNum);
            
            //使用HashMap判断目标值为空的小技巧，取代if else
            if(!colMap.containsKey(colNum)){
                colMap.put(colNum, new ArrayList<Integer>());
            }
            
            colMap.get(colNum).add(current.val);
            
            if(current.left != null){
                nodeQueue.offer(current.left);
                colNumQueue.offer(colNum - 1);
            }
            
            if(current.right != null){
                nodeQueue.offer(current.right);
                colNumQueue.offer(colNum + 1);
            }
            
        }
        
        for(int i = colMin; i <= colMax; i++){
            results.add(colMap.get(i));//这里是shallow copy，不过因为Map中的值并没有改变，所以结果是正确的，面试中跟面试官澄清这一点应该会比较好
        }
        
        return results;
    }
}
```

### 笔记

一开始的感觉是WTF? level order traversal已经不能满足面试官了，又开始发掘新玩法了?

关于思路Grandyang解释的非常简单清晰 [[LeetCode] Binary Tree Vertical Order Traversal 二叉树的竖直遍历](http://www.cnblogs.com/grandyang/p/5278930.html)
```
...那么我们隐约的可以感觉到好像是一种层序遍历的前后顺序，那么我们如何来确定列的顺序呢，我们可以把根节点给个序号0，然后开始层序遍历，凡是左子节点则序号减1，右子节点序号加1，这样我们可以通过序号来把相同列的节点值放到一起，我们用一个map来建立序号和其对应的节点值的映射，用map的另一个好处是其自动排序功能可以让我们的列从左到右，...
```

关于具体的流程leetcode discuss解释的很好 [leetcode - 5ms Java Clean Solution](https://discuss.leetcode.com/topic/31954/5ms-java-clean-solution)
```
* BFS, put node, col into queue at the same time
* Every left child access col - 1 while right child col + 1
* This maps node into different col buckets
* Get col boundary min and max on the fly
* Retrieve result from cols
```
程序实现也是这一篇以及programcreek中的版本都还比较清楚[LeetCode – Binary Tree Vertical Order Traversal (Java)](https://www.programcreek.com/2014/04/leetcode-binary-tree-vertical-order-traversal-java/)


其实程序虽然稍微长了点，但其实明白了核心的思路后，写起来还是不难。整个程序分为两个部分:

1. 通过添枝加叶版的BFS构造一个从colNum到具体val的HashMap，并同时维护min和max来锁定column的范围(因为在一开始并不能预判col的范围是从哪儿到哪儿)
2. 通过min和max来遍历整个HashMap，从而构造最终结果。


注意点:
* 使用一个HashMap，能够通过Column Number来找到对应的各个Node的值
* 可以使用一个Pair类或者两个queue来装Node以及对应的colNum
* 可以设起始的root的colNum为0(其实多少也都行), 然后在bfs的过程中向左伸出子树就-1，向右伸出子树的+1。
* 因为其中提到如果处在同一个row以及同一个col，那么就从左到右，而在BFS的过程中，插入HashMap的顺序正好就可以满足这一点。

时间复杂度和空间复杂度应该都是O(n).