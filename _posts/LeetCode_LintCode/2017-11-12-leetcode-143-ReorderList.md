---
layout: post
title:  "leetcode 143 - Reorder List"
date:   2017-11-12 01:20:39.120390
categories: leetcode, Bloomberg
---

# Reorder List

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
class Solution {
    public void reorderList(ListNode head) {
        
        if(head == null){
            return;
        }
        
        //1. find middle
        
        ListNode fast = head.next;
        ListNode slow = head;
        
        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        
        //2. cut list into 2 halves
        
        ListNode rightHead = slow.next;
        slow.next = null;
        
        //3. reverse second half
        
        ListNode prev = null;
        ListNode temp = null;
        
        while(rightHead != null){
            temp = rightHead.next;
            rightHead.next = prev;
            prev = rightHead;
            rightHead = temp;
        }
        
        rightHead = prev;
        
        // while(prev != null){
        //     System.out.println(prev.val);
        //     prev = prev.next;
        // }
        
        
        //4. merge
        
        ListNode dummyHead = new ListNode(0);
        ListNode resultHead = dummyHead;
        
        int count = 0;
        while(head != null && rightHead != null){
            if(count % 2 == 0){
                resultHead.next = head;
                head = head.next;
            }else{
                resultHead.next = rightHead;
                rightHead = rightHead.next;
            }
            
            resultHead = resultHead.next;
            count++;
        }
        
        //如果list中元素是奇数个，最后会有一个元素需要补刀
        if(head != null){
            resultHead.next = head;
        }else if(rightHead != null){
            resultHead.next = rightHead;
        }
        
    }
}
```

### 笔记

乍一看不知道该咋处理，但一看题解就明白了的题。这题糅杂了find middle，reverse list以及merge，可谓汇聚了所有LinkedList的精华操作，绝对是面试常考题。

只要把4步骤都搞清楚，基本这题大概就没问题了，最后的merge要注意。

**此题如果应该把具体的几个独立的部分分割成不同的method**