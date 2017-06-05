---
layout: post
title:  "LeetCode 221 - Add Two Numbers II"
date:   2017-06-04 00:22:02 -0400
categories: lintcode, Amazon
---

# Add Two Numbers II

## 一刷

### 代码
```java

```

### 笔记


---

## 二刷

### 代码

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;      
 *     }
 * }
 */
public class Solution {
    /**
     * @param l1: the first list
     * @param l2: the second list
     * @return: the sum list of l1 and l2 
     */
    public ListNode addLists2(ListNode l1, ListNode l2) {
        // write your code here
        
        ListNode reversedL1 = reverseList(l1);
        ListNode reversedL2 = reverseList(l2);
        
        boolean carry = false;
        int currentDigit;
        
        ListNode dummy = new ListNode(0);
        ListNode newHead = dummy;
        
        while(reversedL1 != null && reversedL2 != null){
            currentDigit = (reversedL1.val + reversedL2.val + (carry ? 1 : 0)) % 10;
            carry = ((reversedL1.val + reversedL2.val + (carry ? 1 : 0)) / 10) > 0;
            
            newHead.next = new ListNode(currentDigit);
            newHead = newHead.next;
            reversedL1 = reversedL1.next;
            reversedL2 = reversedL2.next;
            
        }
        
        while(reversedL1 != null){
            currentDigit = (reversedL1.val + (carry ? 1 : 0)) % 10;
            carry = ((reversedL1.val + (carry ? 1 : 0)) / 10) > 0;
            newHead.next = new ListNode(currentDigit);
            newHead = newHead.next;
            reversedL1 = reversedL1.next;
        }
        
        while(reversedL2 != null){
            currentDigit = (reversedL2.val + (carry ? 1 : 0)) % 10;
            carry = ((reversedL2.val + (carry ? 1 : 0)) / 10) > 0;
            newHead.next = new ListNode(currentDigit);
            newHead = newHead.next;
            reversedL2 = reversedL2.next;
        }
        
        if(carry){
            newHead.next = new ListNode(1);
            newHead = newHead.next;
        }
        
        return reverseList(dummy.next);
        
    }
    
    private ListNode reverseList(ListNode l1){
        
        ListNode prev = null;
        ListNode next = null;
        
        while(l1 != null){
            next = l1.next;
            l1.next = prev;
            prev = l1;
            l1 = next;
        }
        
        return prev;
    }
    
}
```


### 笔记

这题还真没啥好说的，就是Add Two Numbers和Reverse Linked list的简单结合。

先反转两个参数linkedlist，然后完全按照add two numbers一样的步骤进行计算。最后再把结果翻转就是需要的答案。
