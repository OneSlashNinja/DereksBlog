---
layout: post
title:  "leetcode 24 - Swap Nodes In Pairs"
date:   2017-11-19 22:29:28.516506
categories: leetcode, Microsoft, Bloomberg
---

# Swap Nodes In Pairs

## 一刷

### 代码

iterative版本
```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        head = dummy;
        
        ListNode first = null;
        ListNode second = null;
        ListNode after = null;
        
        //head处于要swap的pair的前一个位置
        while(head.next != null && head.next.next != null){
            //先标记位置
            first = head.next;
            second = head.next.next;
            after = head.next.next.next;
            
            //然后进行swap
            head.next = second;
            second.next = first;
            first.next = after;
            
            head = first;//此时的first相当于swap后的second，head处在这个位置为下个pair做准备
        }
        
        return dummy.next;
    }
}
```

recursion版本
```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        
        //head == null || head.next == null就凑不成pair，也就没必要reverse了
        if(head == null || head.next == null){
            return head;
        }
        
        ListNode temp = head.next;
        head.next = swapPairs(head.next.next);//接下来的事儿交给recursion，就假装它啥都已经搞定啦
        temp.next = head;
        
        return temp;
    }
}
```

### 笔记

此题可以使用recursion的版本也可以使用iterative的版本。

可以看见，recursion的版本比iterative的代码量少很多，甚至都不需要使用dummy node。非常巧妙。

对于iterative的版本，不太知道怎么使用最少量的临时ListNode指针的话索性就使用三个，first, second, after。看着也直观。