---
layout: post
title:  "LeetCode 206 - Reverse Linked List"
date:   2017-05-30 00:02:02 -0400
categories: leetcode, Amazon
---

# Title

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
     * @param head: The head of linked list.
     * @return: The new head of reversed linked list.
     */
    public ListNode reverse(ListNode head) {
        // write your code here
        ListNode prev = null;
        ListNode temp = null;
        while(head != null){
            temp = head.next;
            head.next = prev;
            prev = head;
            head = temp;
        }
        
        return prev;
    }
}
```

### 笔记

代码很短，主要要想清楚每一步到底干了啥。并且reverse的作为一个基本操作，在解其他题的时候也会很有用。

一开始自己想的思路是先把整个linked list按顺序copy到一个数组里，然后逆向再生成一个新的LinkedList，就是reversed linkedList。但是这样其实并不是将原来的链表反转，而是生成了一个新的链表，并且还额外使用O(n)空间的数组。

其实反转很简单，就是将链表所有的next“调转枪头”。但是为了完成蒸锅过程，需要两个辅助的ListNode：
prev：一直比head后一位，用来指引“调转枪头”后到底指哪儿。
temp：用来做buff。为什么需要它？因为我们一方面需要按照Linkedlist原来的顺序进行遍历。但是另一方面又需要对每个node“调转枪头”。而调转枪头后head.next就不再是原来顺序的下一个了。所以我们需要一个buff先把“调转枪头”前的head.next暂存起来，等到调转枪头之后再赋给head。


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
    public ListNode reverseList(ListNode head) {
        
        ListNode prev = null;
        ListNode next = null;
        
        while(head != null){
            next = head.next;
            head.next = prev;
            prev = head;
            head = next;
        }
        
        return prev;
        
    }
}
```

### 笔记
这其实已经是刷的第n遍了，发现虽然记住了**while循环中一个环，并且要调转枪头**，但还是不能特别好的记住到底怎么调转的。

所以就记住额外增加了两个辅助的ListNode，一个指head前面的，一个指head后面的，所以就起名叫prev和next。初始化都是null。

并且要注意的是最后返回的是prev，因为head已经指到null去了。