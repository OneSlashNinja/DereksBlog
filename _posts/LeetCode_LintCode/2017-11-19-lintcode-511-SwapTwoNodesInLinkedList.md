---
layout: post
title:  "lintcode 511 - Swap Two Nodes In Linked List"
date:   2017-11-19 23:24:49.951110
categories: lintcode, EMC
---

# Swap Two Nodes In Linked List

## 一刷

### 代码

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

public class Solution {
    /*
     * @param head: a ListNode
     * @param v1: An integer
     * @param v2: An integer
     * @return: a new head of singly-linked list
     */
    public ListNode swapNodes(ListNode head, int v1, int v2) {
        // write your code here
        
        if(head == null){
            return null;
        }
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        
        ListNode result1Prev = findNodePrev(dummy, v1);
        ListNode result2Prev = findNodePrev(dummy, v2);
        
        //有可能v1或者v2根本就找不到，就没必要swap了
        if(result1Prev == null || result2Prev == null){
            return head;
        }
        
        ListNode result1 = result1Prev.next;
        ListNode result2 = result2Prev.next;
        ListNode result1After = result1.next;
        ListNode result2After = result2.next;
        
        //一定要注意这种两个node相邻的情况，这里cover val1 = > val2
        if(result1.next == result2){
            result1Prev.next = result2;
            result2.next = result1;
            result1.next = result2After;
            return dummy.next;
        }
        
        //一定要注意这种两个node相邻的情况，这里cover val2 = > val1
        if(result2.next == result1){
            result2Prev.next = result1;
            result1.next = result2;
            result2.next = result1After;
            return dummy.next;
        }
        
        result1Prev.next = result2;
        result2.next = result1After;
        
        result2Prev.next = result1;
        result1.next = result2After;
        
        return dummy.next;//注意是dummy.next而不是head。因为头部有可能被替换
    }
    
    //因为要替换，所以需要prev，而不仅是node本身
    private ListNode findNodePrev(ListNode head, int val){
        
        while(head != null && head.next != null){
            if(head.next.val == val){
                return head;
            }
            head = head.next;
        }
        
        return null;
    }
    
}
```

### 笔记

这是一道看似很straightforward，但实际上暗藏各种陷阱的题目。

就像GeeksforGeeks中提到的:

```
This may look a simple problem, but is interesting question as it has following cases to be handled.
1) x and y may or may not be adjacent.
2) Either x or y may be a head node.
3) Either x or y may be last node.
4) x and/or y may not be present in linked list.
```

其中的2，3，4自己都提前想到了。2使用dummy node就可以处理，3其实不需要处理。4的话只要搜索结果之一为null就直接不同swap了。

而最想不到的情况就是1: x and y may or may not be adjacent.

你会发现如果两个node相邻的话，比如:
10->15->12->13->20->14,  x = 12, y = 13
那么直接使用general的swap会出问题，某个node的Next会指向它自己(纸上画一画)

所以需要程序中需要三道filter才能放心进行最general的swap。