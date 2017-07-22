---
layout: post
title:  "LeetCode 21 - Merge Two Sorted Lists"
date:   2017-05-21 00:22:02 -0400
categories: leetcode, Amazon
---

# Merge Two Sorted Lists

## 一刷

### 代码
```java
/**
 * Definition for ListNode.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int val) {
 *         this.val = val;
 *         this.next = null;
 *     }
 * }
 */ 
public class Solution {
    /**
     * @param ListNode l1 is the head of the linked list
     * @param ListNode l2 is the head of the linked list
     * @return: ListNode head of linked list
     */
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        // write your code here
        
        ListNode dummy = new ListNode(0);
        
        ListNode head = dummy;
        
        while(l1 != null && l2 != null){
            if(l1.val < l2.val){
                head.next = l1;
                l1 = l1.next;
                head = head.next;
            }else{
                head.next = l2;
                l2 = l2.next;
                head = head.next;
            }
        }
        
        if(l1 != null){
            head.next = l1;
        }
        
        if(l2 != null){
            head.next = l2;
        }
        
        return dummy.next;
        
    }
}
```

### 笔记
不知道这道题其实之前做过很多次了，都是作为其他题的基础操作了，比如Merge k Sorted Lists。总之没什么好说的，一遍(除了一个小typo)bug free过。

---

## 二刷

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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode head = dummy;
        
        while(l1 != null && l2 != null){
            if(l1.val <= l2.val){
                //(1)注意顺序
                //(2)注意l1和head都要前进
                //(3)循环每次只处理一个node，并不是小的大的按顺序一次都加进来
                head.next = l1;
                l1 = l1.next;
                head = head.next;
            }else{
                head.next = l2;
                l2 = l2.next;
                head = head.next;
            }
        }
        
        //使用while多余了，直接把剩下的接在后面就可以
        //while(l1 != null){
        //    head.next = l1;
        //    l1 = l1.next;
        //    head = head.next;
        //}
        if(l1 != null){
            head.next = l1;
        }

        //while(l2 != null){
        //    head.next = l2;
        //    l2 = l2.next;
        //    head = head.next;
        //}
        if(l2 != null){
            head.next = l2;
        }
        
        return dummy.next;
    }
}
```


### 笔记

二刷的时候大体的结构记的都不错，但是犯了一个很不该犯的错误：
**在merge的时候循环中每次只拿去较小的那个node，较大的仍然吧保留，以待循环的下一次进行比较**